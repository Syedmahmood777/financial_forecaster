# Financial Forecaster: Project Overview
* Creating a model which learns to forecast future transactions for your account.
* Exploratory Data Analysis (EDA) is done to understand and gain insights from the data.
* Previous bank statements are used to collect the data.
* Refining and cleaning of data takes place for better use.
* Time series model is fitted on the data for forecasting.

## Code and Resources Used
**Python Version**: 3.10.9  
**Jupyter Lab Version**: 3.5.3  
**Packages**: pandas, numpy, matplotlib, seaborn, pmdarima, statsmodels, scipy    
**Project Format**: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t  
**SARIMAX Article**: https://towardsdatascience.com/time-series-forecasting-with-arima-sarima-and-sarimax-ee61099e78f6  
**Markdown Cheatsheet**: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet  

## Data Collection
* Bank statements are used to collect data of transactions.
* It consists of Date Of Transaction, Transaction Amount, Type of Transaction, Deposit/ Withdrawl.
* Data collection is done for as long duration as possible for better results.
* All the data is imported in an excel file for further processing using pandas in python.

## Data Cleaning
After collection of data, I needed to clean to remove unwanted values and anything that will hinder its perfomance
* Data collected is clean for better analysis and understanding.
* Removing of null values, creating new columns for UPI transactions.
* Converting multiple transactions on a day to single transaction for further processing.
* Calculating monthly transactions and importing a new dataframe based on it.  

## EDA
Exploratory Data Analysis is done on both Daily, Monthly Transactions  

![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/src_img/upi_transactions.png "UPI Transactions.png")  
![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/src_img/tot_deposits.png "Total_Deposits.png")  
<p align="center">Kernel Density Estimate Of Monthly Withdrawls</p>  

![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/src_img/kde_with.png "KDE Withdrawls.png")  

## Time Series Analysis
* Analysing all the transactions with respect to date
* Using two models to gain best results
* ARIMA model without seasonality
* SARIMAX model with seasonality to learn trends

## Arima Model
Arima model was applied, but its results were static.  
![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/model_analysis/arima_model.png " arima model.png")  
Errors of the model were as follows:  
* Mean Absolute Error: 3282.0327896414537  
* Mean Absolute Percentage Error: 3.022257511793852e+18  
* Root Mean Squared Error: 5817.4732058623495  
![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/model_analysis/arima_pred.png " arima pred.png")  

## SARIMAX Model
SARIMAX model was applied for better result and understanding seasonality:  
![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/model_analysis/sarima_model.png " sarima model.png")  
Errors of the model were as follows:  
* Mean Absolute Error: 3971.822417234379  
* Mean Absolute Percentage Error: 4.645845057110243e+18  
* Root Mean Squared Error: 5697.147329455461  
![alt text](https://github.com/Syedmahmood777/financial_forecaster/blob/main/model_analysis/sarima_pred.png " sarima pred.png")  





