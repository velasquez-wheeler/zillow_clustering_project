import numpy as np
import pandas as pd

import env

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

