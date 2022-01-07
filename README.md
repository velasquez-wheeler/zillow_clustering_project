# About this Project

## Project Goals
The goal of this project is to assess features of real estateto find meaningful clusters for use in predicting logerror.


## Project Description

With low interest rates and a strong buyer's market, it is increasingly important to identify valuable real estate investment opportunities. Zillow's zestimate modeling may be improved with input from the open-source community to better predict home values and reduce logerror.

## Initial Questions

- What can we cluster?
    - bed/bath/sqft
    - lat/long/age/fips/acres
    - structuretax/taxvaluedollar/landtax/taxamount/acres
    - acres/sqft
    - bed/bath/taxvalue
- What drives logerror?
    - Bed/bath/sqft Clusters
    - Bedroom count
    - Bathroom count
    - Finished sqft
    - FIPS

## Data Dictionary

| variable      | meaning       |
| ------------- |:-------------:|
|logerror|target value: log(zestimate) - log(sale price)
|lm|Ordinary Least Squares Linear Regression modeling algorithm|
|lm2|Polynomial Regression modeling algorithm |
|lars|Lasso + Lars Regression modeling algorithm|
|glm|TweedieRegressor modeling algorithm|
|df|Dataframe of raw zillow data from sql server|
|train| training dataset, a major cut from the df|
|validate| validate dataset, used to prevent overfitting|
|test| test dataset, to test the top model on unseen data|
|pearsonr| statistical test used to compare churn with various categories|
|taxvaluedollarcnt| The assessed value of the built structure on the parcel|
|calculatedfinishedsquarefeet| Calculated total finished living area of the home |
|structuretaxvaluedollarcnt| assessed value of the structure|
|landtaxvaluedollarcnt|assessed value of the land|
|taxamount|total property tax assessed for that year|
|bedroomcnt| Number of bedrooms in home |
|bathroomcnt| Number of bathrooms in home including fractional bathrooms|
|latitude/longitude| coordinates of the property|
|acres| lotsizesquarefeet / 43560|
|age| 2017 - yearbuilt|
|dollar_per_acre| landtaxvaluedollarcnt / acres|
|dollar_per_sqft| structuretaxvaluedollarcnt / calculatedfinishedsquarefeet|
|features_cluster|cluster created with features of the property|
|value_cluster|cluster created with dollar features|
|development_cluster|cluster created with location and age data|
|fips| County codes for property locations|
| County Codes||
|6037 | Los Angeles, CA|
|6059 | Orange, CA|
|6111 | Ventura, CA|


## Steps to Reproduce 
What I did to get here?
- Create Trello Board listing tasks to completion
- Created modules with functions to acquire and clean the data
- Examined the data and came up with 4 questions
- Created visualizations relating to the quesitons
- Ran statistical tests to answer the questions
- Create clustirs and explore them 
- Created a baseline model to test baseline accuracy
- Created numerous models to see how various algorithms performed
- Modified algorithms to see how changes affected performance
- Chose the 4 that performed the best and evaluated them on the validate training set
- Best performing model evaluated against test
- Decided on a recommendation and next steps
- Turn in final Jupyther Notebook

## The Plan

### Wrangle
- wrangle.py
Functions to acquire, clean, tidy, prepare, split, and scale the data for use.

### Explore
#### Ask Questions
- What can we cluster?
    1. bed/bath/sqft
    2. lat/long/age/fips/acres
    3. structuretax/taxvaluedollar/landtax/taxamount/acres
    4. acres/sqft
    5. bed/bath/taxvalue
- What drives logerror?
    1. Bed/bath/sqft Clusters
    2. Bedroom count
    3. Bathroom count
    4. Finished sqft
    5. FIPS

#### Visualizations
- Matplotlib and Seaborn used to create visualizations

#### Statistical Tests
Used .mean(), t-test, and pearsonr to answer statistical questions

#### Summary
Wrap up all of the testing conclusions

### Clustering

Use sklearn cluster KMeans

### Modeling
#### Select Evaluation Metric

#### Evaluate Baseline

#### Develop 3 Models

#### Evaluate on Train
All models evaluated on train, but top 4 were validated

#### Evaluate on Validate
Ensure no overfitting takes place

#### Evaluate top model on Test
Top model evaluated against test dataset to see how it performed on unknown data.