import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import env


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import pandas as pd
import numpy as np
import os
from env import host, user, password

####### Acquire #######
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
    
def new_zillow_data():
    '''
    This function reads all tables and columns into a dataframe, including only properties with lat/long
    data and had transactions in 2017. Properties with multiple transactions 
    will display only the most recent transaction.
    '''
    sql_query = """
                SELECT p.*, m.logerror, m.transactiondate, ac.airconditioningdesc, arch.architecturalstyledesc, b.buildingclassdesc, heat.heatingorsystemdesc, pt.propertylandusedesc, s.storydesc, c.typeconstructiondesc
                FROM properties_2017 as p
                JOIN predictions_2017 as m USING(parcelid)
                LEFT JOIN airconditioningtype as ac USING(airconditioningtypeid)
                LEFT JOIN architecturalstyletype as arch USING(architecturalstyletypeid)
                LEFT JOIN buildingclasstype as b USING(buildingclasstypeid)
                LEFT JOIN heatingorsystemtype as heat USING(heatingorsystemtypeid)
                LEFT JOIN propertylandusetype as pt USING(propertylandusetypeid)
                LEFT JOIN storytype as s USING(storytypeid)
                LEFT JOIN typeconstructiontype as c USING(typeconstructiontypeid)
                LEFT JOIN unique_properties as u USING(parcelid)
                INNER JOIN (SELECT p.parcelid, MAX(transactiondate) AS maxdate FROM properties_2017 as p JOIN predictions_2017 USING(parcelid) GROUP BY p.parcelid, logerror) md ON p.parcelid = md.parcelid AND transactiondate = maxdate
                WHERE transactiondate LIKE '2017%%' AND latitude IS NOT NULL AND longitude IS NOT NULL
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df

def get_zillow_data():
    '''
    This function reads in zillow data from the Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('zillow.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_zillow_data()
        
        # Cache data
        df.to_csv('zillow.csv')
        
    return df




###### Prepare #######
def handle_missing_values(df, prop_required_column = .5, prop_required_row = .70):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def drop_cols(df, cols_to_drop):
    df.drop(columns = cols_to_drop, inplace = True)
    return df

    
####### Prepare ########    

def min_max_scaler(train, validate, test):
    '''
    Takes train, validate, and test dataframes as arguments and returns
    min-max scaler object and scaled versions of train, validate, and test.
    '''
    scaled_vars = list(train.select_dtypes('number').columns)
    scaled_column_names = [i for i in scaled_vars]
    scaler = MinMaxScaler(copy=True, feature_range=(0,1))
    train_scaled = scaler.fit_transform(train[scaled_vars])
    validate_scaled = scaler.transform(validate[scaled_vars])
    test_scaled = scaler.transform(test[scaled_vars])

    train_scaled = pd.DataFrame(train_scaled, columns=scaled_column_names, index=train.index.values)
    validate_scaled = pd.DataFrame(validate_scaled, columns=scaled_column_names, index=validate.index.values)
    test_scaled = pd.DataFrame(test_scaled, columns=scaled_column_names, index= test.index.values)
    return scaler, train_scaled, validate_scaled, test_scaled

def remove_outliers_iqr(df, k, col_list):
    ''' 
    Takes in a df, k, and list of columns returns
    a df with removed outliers
    '''
    
    for col in col_list:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles
        
        iqr = q3 - q1   # calculate interquartile range
        
        upper_bound = q3 + k * iqr   # get upper bound
        lower_bound = q1 - k * iqr   # get lower bound

        # return dataframe without outliers
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    return df


######## Wrangle ##########

def wrangle_zillow():
    # acquire df
    df = get_zillow_data()
    # only single family
    df = df[df.propertylandusetypeid == 261]
    # at least 1 bed and bath and 350 sqft
    df = df[(df.bedroomcnt > 0) & (df.bathroomcnt > 0) & (df.calculatedfinishedsquarefeet>350)]
    # handle missing values
    df = handle_missing_values(df)
    # fill lotsize
    df.lotsizesquarefeet.fillna(7313, inplace = True)
    # create acre feature
    df['acres'] = df.lotsizesquarefeet/43560
    # create age feature
    df['age'] = 2017 - df.yearbuilt
    # create $/sqft
    df['dollar_per_sqft'] = df.structuretaxvaluedollarcnt/df.calculatedfinishedsquarefeet
    # create $/acre
    df['dollar_per_acre'] = df.landtaxvaluedollarcnt/df.acres
    # drop unnecessary columns
    df = drop_cols(df, ['id','calculatedbathnbr', 'buildingqualitytypeid','finishedsquarefeet12', 'fullbathcnt', 'heatingorsystemtypeid','heatingorsystemdesc','propertycountylandusecode', 'propertylandusetypeid','propertyzoningdesc',  'censustractandblock', 'propertylandusedesc', 'unitcnt','lotsizesquarefeet','assessmentyear','yearbuilt','rawcensustractandblock','roomcnt'])
    # properties under 5 million USD
    df = df[df.taxvaluedollarcnt < 5_000_000]
    # add counties
    df['county'] = np.where(df.fips == 6037, 'Los_Angeles',np.where(df.fips == 6059, 'Orange', 'Ventura'))  
    # catch other nulls
    df.dropna(inplace=True)
    # remove outliers
    df = df[((df.bathroomcnt <= 7) & (df.bedroomcnt <= 7) & 
            (df.regionidzip < 100000) & 
            (df.bathroomcnt >= 0) & 
            (df.bedroomcnt > 0) &
            (df.taxamount < 15000) &
            # (df.structuretaxvaluedollarcnt < 2000000) &
            (df.acres < 1.5) &
            (df.calculatedfinishedsquarefeet <= 4000)
#                (df.taxrate < 10)
              )]
    # return wrangled df
    return df
 

######## Split ########
def split_data(df):
    '''
    Takes in a dataframe and returns train, validate, and test subset dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state = 333)
    train, validate = train_test_split(train, test_size = .3, random_state = 333)
    return train, validate, test