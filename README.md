# About this Project

## Project Goals
1. Discover drivers of log error of Zestimate to determine how current model could potentially be improved
2. To cluster features to predict logerror
3. Turn in a Jupiter notebook and multiple moduels that will clearly demostrate the precess and how it can be replicated by anyone with propper credentials to acess the Zillow database

## Project Description

Zillow is asking our team to predict the log-error between their Zestimate and the actual sale price, given atleast three the features of a home.

 The log error is defined as

𝑙𝑜𝑔𝑒𝑟𝑟𝑜𝑟=𝑙𝑜𝑔(𝑍𝑒𝑠𝑡𝑖𝑚𝑎𝑡𝑒 −𝑙𝑜𝑔(𝑆𝑎𝑙𝑒𝑃𝑟𝑖𝑐𝑒)

In this project, you are going to predict the logerror for the year 2017.

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