
#Imports
import pandas as pd
import numpy as np


#Imporitng Refined Statement (Adding additional columns after dropping null values)
df=pd.read_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\reformatted_statements.csv')

#Seperate Database for Withdrawl and payment type
transactions_df=pd.DataFrame(data=df.iloc[:,[0,1,3]].values,columns=['Date','Withdrawls','UPI'])
deposits_df=pd.DataFrame(data=df.iloc[:,[0,2]].values,columns=['Date','Deposits'])


#Replacing input mistakes of UPI labels
transactions_df['UPI']=transactions_df['UPI'].apply(lambda x: x.replace('ysyes','yes'))


#Getting dummies for better analysis of UPI transactions
data=pd.get_dummies(transactions_df['UPI'])

#Ordering dummy columns
data.rename(columns={'no':'No','yes':'Yes'},inplace=True)
data=data[['Yes','No']]


#Removing existing UPI column and adding dummy columns
transactions_df=transactions_df.drop('UPI',axis=1)
transactions_df=transactions_df.join(data)


#Preprocessing
# #Dropping Null Values & Removing unicode formats
transactions_df.dropna(axis=0,inplace=True)
transactions_df=transactions_df[transactions_df['Withdrawls']!='0']

deposits_df.dropna(axis=0,inplace=True)
deposits_df['Deposits']=deposits_df['Deposits'].apply(lambda x: x.replace('\xa0','0').replace(' ','0'))
deposits_df=deposits_df[deposits_df['Deposits']!='0']


#Some values of data are in string format
#Checking types of data
# print(transactions_df.dtypes)



#All the data types are strings(objects), converting Withdrawls, Deposits into int
#Since commas were causing errors, removing it helps the data to convert easily
transactions_df['Withdrawls']=transactions_df['Withdrawls'].str.replace(',','').astype(float)
deposits_df['Deposits']=deposits_df['Deposits'].str.replace(',','').astype(float)


#Withdrawls type is changed to int32 successfully
#print(transactions_df.dtypes)



#Monthly & Daily Transactions (Withdrawls & Deposits monthly)
#Total transactions and number of upi transactions are also noted for better insights
daily_transactions=pd.DataFrame(data=np.array(pd.date_range(start="2022/04/01",end="31/03/2023",).strftime('%Y-%m-%d')),columns=["Date"])
daily_transactions[["Withdrawls","Total","Yes","No"]]=0

# daily_transactions=pd.DataFrame(columns=["Date",'Withdrawls','Total','Yes','No'])

monthly_transactions=pd.DataFrame(columns=["Date",'Withdrawls','Total','Yes','No'])

import datetime

#Array of all the different dates/months since there are multiple transactions on a single day 
unique_dates=transactions_df['Date'].unique()

#Loop for adding all the values in a single day

for i in unique_dates:
    daily_value=transactions_df.loc[transactions_df['Date']==i,'Withdrawls'].sum()
    count=len(transactions_df.loc[transactions_df['Date']==i])      #Number of transactions
    tr_yes=len(transactions_df.loc[(transactions_df['Date']==i) & (transactions_df['Yes']==True) ])
    tr_no=len(transactions_df.loc[(transactions_df['Date']==i) & (transactions_df['No']==True) ])
    ndate=datetime.datetime.strptime(i, "%m/%d/%Y").date()
    newtransaction={'Date':i,'Withdrawls':daily_value,'Total':count,'Yes':tr_yes,'No':tr_no}
    # daily_transactions.loc[len(daily_transactions)]=newtransaction
    daily_transactions.loc[daily_transactions['Date']==ndate.strftime('%Y-%m-%d')]=[ndate.strftime('%Y-%m-%d'),daily_value,count,tr_yes,tr_no]

# not_da=daily_transactions.loc[daily_transactions["Withdrawls"]!=0]
# not_da=daily_transactions.dropna(axis=0,inplace=False)
#tr_yes is used to keep count for all the transactions with 'UPI' dummy values, we created earlier
#tr_no is used to keep count for all the transactions without 'UPI' dummy values.

#Unique Months would be a little more difficult since we have to split at months only
#to get unique keys






unique_months = pd.period_range("2022-04", "2023-03", freq='M')
#Above output will be in a format of Month/Year (04/2022)



#Loop for adding all the values in a single month
for i in unique_months:
   
    
    monthly_value=daily_transactions.loc[daily_transactions['Date'].apply(lambda x:x.rsplit('-',1)[0])==i.strftime("%Y-%m"),'Withdrawls'].sum()
  
    count=daily_transactions.loc[daily_transactions['Date'].apply(lambda x:x.rsplit('-',1)[0])==i.strftime("%Y-%m"),"Total"].sum()      #Number of transactions
    tr_yes=daily_transactions.loc[daily_transactions['Date'].apply(lambda x:x.rsplit('-',1)[0])==i.strftime("%Y-%m"),"Yes"].sum()
    tr_no=daily_transactions.loc[daily_transactions['Date'].apply(lambda x:x.rsplit('-',1)[0])==i.strftime("%Y-%m"),"No"].sum()
   
   
    
    newtransaction={'Date':i,'Withdrawls':monthly_value,'Total':count,'Yes':tr_yes,'No':tr_no}
    monthly_transactions.loc[len(monthly_transactions)]=newtransaction
   
    
#Multiple splitting of date is due to our '04/2022' format hence, we are only matching first element
#which is the month of transaction '04' with unique keys of each month



#Similarly, we are going to create a dataframe for monthly deposits since
#daily deposits isn't a thing
monthly_deposits=pd.DataFrame(columns=["Date",'Deposits','Total'])
unique_months=deposits_df['Date'].apply(lambda x:x.split('/',1)[0]+'/'+x.split('/')[2]).unique()

for i in unique_months:
    monthly_value=deposits_df.loc[deposits_df['Date'].apply(lambda x:x.split('/',1)[0])==i.split('/',1)[0],'Deposits'].sum()
    count=len(deposits_df.loc[deposits_df['Date'].apply(lambda x:x.split('/',1)[0])==i.split('/',1)[0]])      #Number of transactions
    newtransaction={'Date':i,'Deposits':monthly_value,'Total':count}
    monthly_deposits.loc[len(monthly_deposits)]=newtransaction









daily_transactions.to_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\daily_transactions.csv',index=False)
monthly_transactions.to_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\monthly_transactions.csv',index=False)
# transactions_df.to_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\transactions_upi.csv',index=False)
# deposits_df.to_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\deposits.csv',index=False)
monthly_deposits.to_csv(r'C:\Users\WELCOME\Desktop\financial_forecaster\monthly_deposits.csv',index=False)
          
deposits_df.reset_index()
del tr_yes
del tr_no
del df
del count
del data             
del unique_dates
del unique_months
del i
del monthly_value
del newtransaction
del daily_value
