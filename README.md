# Financial Forecaster: Project Overview
* Creating a model which learns to forecast future transactions for your account.
* Exploratory Data Analysis (EDA) is done to understand and gain insights from the data.
* Previous bank statements are used to collect the data.
* Refining and cleaning of data takes place for better use.
* Time series model is fitted on the data for forecasting.

## Code and Resources Used
**Python Version**: 3.10.9  
**Jupyter Lab Version**: 3.5.3  
**Packages**: pandas, numpy, matplotlib, seaborn, pmdarima, statsmodels    
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

<!-- ## EDA
Exploratory Data Analysis is done on both Daily, Monthly Transactions -->
