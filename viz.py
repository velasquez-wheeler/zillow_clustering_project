import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# supress scientific notation
np.set_printoptions(suppress=True)

from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings("ignore")
# ---------------------------------

# visualize features for outliers
def features_outliers(x):
    for col in x.columns:
        sns.boxplot(x[col])
        plt.title(col)
        plt.show()
        
#visualization of Log Error by fip        
def log_error_by_fip(train):
    return sns.barplot(data = train, x = 'fips', y = 'logerror')

# pseudo map of data
def data_map(train):
    sns.scatterplot(x='longitude',y='latitude',data=train, \
                    hue = 'landtaxvaluedollarcnt', palette = 'turbo',alpha = 0.8 )

# elbow method to find k for closter 1
def cluster1_elbow_for_k(X_train_feature_cluster):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(10, 10))
        pd.Series({k: KMeans(k).fit(X_train_feature_cluster).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
        
# elbow method to find k in cluster 2
def cluster2_elbow_for_k(X_train_value_cluster):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(10, 10))
        pd.Series({k: KMeans(k).fit(X_train_value_cluster).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
       
# ------------------------- Cluster1 viz -------------------------------------
    
# clusters with k = 4 to 7 
def clusterwit_n_k(X_train_feature_cluster):
    fig, axs = plt.subplots(2, 2, figsize=(13, 13), sharex=True, sharey=True)

    for ax, k in zip(axs.ravel(), range(4, 8)):
        clusters = KMeans(k).fit(X_train_feature_cluster).predict(X_train_feature_cluster)
        ax.scatter(X_train_feature_cluster.taxvaluedollarcnt, X_train_feature_cluster.calculatedfinishedsquarefeet, c=clusters)
        ax.set(title='k = {}'.format(k), xlabel='taxvaluedollarcnt', ylabel='calculatedfinishedsquarefeet')
        
# visualize clusters with their centroids
def cluster1_centroid(X_train_feature_cluster, centroids):
    # visualize clusters with their centroids
    plt.figure(figsize = (14,14))
    sns.scatterplot(data = X_train_feature_cluster, x = 'taxvaluedollarcnt', y = 'calculatedfinishedsquarefeet', hue = 'feature_cluster', s = 100, alpha = 0.7, palette = 'turbo')
    centroids.plot.scatter(x='taxvaluedollarcnt',y='calculatedfinishedsquarefeet',ax = plt.gca(), color = 'black',alpha = 0.5, s=300, label = 'centroid')
    plt.title('Properties by Tax Value and Square Footage')
    plt.legend(loc = 'upper right')

# visualize clusters against bathrooms vs taxvaluedollarcnt
def cluster_bathroom_vs_taxvalue(X_train_feature_cluster, centroids):
    plt.figure(figsize = (14,14))
    sns.scatterplot(data = X_train_feature_cluster, x = 'bathroomcnt', y = 'taxvaluedollarcnt', hue = 'feature_cluster', s = 100, alpha = 0.7, palette = 'turbo')
    centroids.plot.scatter(x='bathroomcnt',y='taxvaluedollarcnt',ax = plt.gca(), color = 'black',alpha = 0.5, s=300, label = 'centroid')
    plt.title('Properties by Bedroom and Bathroom Count')
    plt.legend(loc = 'upper left')
   

# ------------------------- Cluster2 viz -------------------------------------


# elbow method to find k for cluster 2
def cluster2_elbow_for_k(X_train_value_cluster):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(10, 10))
        pd.Series({k: KMeans(k).fit(X_train_value_cluster).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
        
# # visualize CLUSTER 2 structuretax/taxvaluedollar/landtax/taxamount
def cluster2_with_centroid(X_train_value_cluster, centroids):
    plt.figure(figsize = (14,14))
    sns.scatterplot(data = X_train_value_cluster, x = 'taxvaluedollarcnt', y = 'taxamount', hue = 'value_cluster', s = 100, alpha = 0.7, palette = 'turbo')
    centroids.plot.scatter(x='taxvaluedollarcnt',y='taxamount',ax = plt.gca(), color = 'black',alpha = 0.5, s=300, label = 'centroid')
    plt.title('Tax Value Clusters')
    plt.legend(loc = 'upper right')
        
# ------------------------- Cluster3 viz -------------------------------------

# cluster 3elbow method to find k
def cluster3_elbow_for_k(X_train_value_cluster):
    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(10, 10))
        pd.Series({k: KMeans(k).fit(X_train_value_cluster).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
        
# visualize cluster 3 lat/long, 
def cluster3_with_centroid(X_train_development_cluster, centroids):
    plt.figure(figsize = (14,14))
    sns.scatterplot(data = X_train_development_cluster, x = 'longitude', y = 'latitude', hue = 'development_cluster', s = 100, alpha = 0.7, palette = 'turbo')
    centroids.plot.scatter(x='longitude',y='latitude',ax = plt.gca(), color = 'black',alpha = 0.5, s=300, label = 'centroid')
    plt.title('Tax Value Clusters')
    plt.legend(loc = 'upper right')

# ------------------------- Shape of data -------------------------------------

def shape(train_scaled):
    for col in train_scaled.columns:
        plt.figure(figsize=(10,10))
        plt.hist(train_scaled[col])
        plt.title(col)
        
# ------------------------- All Models Comparison on Validate -------------------------------------        

# plot to visualize actual vs predicted.
def model_compare(y_validate):
    plt.figure(figsize=(16,8))
    plt.hist(y_validate.logerror, color='blue', alpha=.5, label="Actual Log Error")
    plt.hist(y_validate.logerror_pred_lm, color='red', alpha=.5, label="Model: LinearRegression")
    plt.hist(y_validate.logerror_pred_glm, color='yellow', alpha=.5, label="Model: TweedieRegressor")
    plt.hist(y_validate.logerror_pred_lars, color='orange', alpha=.5, label="Model: LassoLars")
    plt.hist(y_validate.logerror_pred_lm2, color='green', alpha=.5, label="Model 2nd degree Polynomial")
    plt.title("Comparison of the models using all the features")
    plt.xlabel("Log Error")
    plt.ylabel("Number of Homes")
    plt.title("Comparing the Distribution of Actual Log Error to Distributions of Predicted Log Error All Models")
    plt.legend()
    plt.show()

def RMSE_all_models(y_validate):
    RMSE_compare = pd.DataFrame(y_validate.mean(axis=0))
    RMSE_compare = RMSE_compare.reset_index()
    RMSE_compare = RMSE_compare.rename(columns={0 : "RMSE", 'index' : 'Model'})
    sns.barplot(data=RMSE_compare, x='RMSE', y='Model')
    plt.title('2 Models do better than baseline, but not Logerror')

# ------------------------- Linear Regression Model Comparison on Test -------------------------------

# compare actual Logerror against Linear Regression model
def best_model_vs_logerror(y_test):
    plt.figure(figsize=(18,10))
    plt.hist(y_test.logerror, color = 'blue',alpha = 0.5, label = 'Actual Log Error')
    plt.hist(y_test.logerror_pred_lm, color = 'red',alpha=0.5,label='Model: Linear Regression')
    plt.xlabel("Log Error")
    plt.ylabel("Number of Homes")
    plt.title("Comparing the Distribution of Actual Log Error to Distributions of Predicted Log Error for the Top Model")
    plt.legend()
    plt.show();
    
    
# Linear Regression prediction vs actual Loogerror and baseline
def actal_logerror_vs_predicted_OLS(y_test):
    plt.figure(figsize=(15,10))
    plt.plot(y_test.logerror, y_test.logerror, alpha=.5, color="blue", label='Predict = Actual Log Error')
    plt.plot(y_test.logerror, y_test.logerror_pred_lm, alpha=.5, color="gray", label='Predict using mean')
    plt.scatter(y_test.logerror, y_test.logerror_pred_lm, 
                alpha=.9, color="Yellow", s=100, label="Model: OLS (Linear regression)")
    plt.legend()
    plt.xlabel("Actual Log Error")
    plt.ylabel("Predicted Log Error")
    plt.title("OLS (Linear regression) on Test Data, Actual vs. Predicted")
    plt.show()
    
# Visual for residual error
def resiudal_error(y_test):
    plt.figure(figsize=(15,10))
    plt.axhline(label="No Error")
    plt.scatter(y_test.logerror, y_test.logerror_pred_lm - y_test.logerror, 
                alpha=.9, color="yellow", s=100, label="Model: Liner Regression")
    plt.legend()
    plt.xlabel("Actual Log Error")
    plt.ylabel("Residual/Error: Predicted Log Error - Actual Log Error")
    plt.title("OLS (Linear Regression) Residual Error")
    plt.show()


