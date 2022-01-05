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

- 
- 
- 
- 

## Data Dictionary

| variable      | meaning       |
| ------------- |:-------------:|
|insert label|insert description|


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
1. 
2. 
3. 
4. 

#### Visualizations
- Matplotlib and Seaborn used to create visualizations

#### Statistical Tests
Used .mean(), t-test, and pearsonr to answer statistical questions

#### Summary
Wrap up all of the testing conclusions

### Clustering


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