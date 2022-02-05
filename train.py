# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 16:41:20 2022

@author: siva
"""

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score,mean_squared_error

from sklearn.preprocessing import OneHotEncoder

import pickle

path='C:\\Users\\siva\\Documents\\Great learning\\datasets'

df=pd.read_csv(path+'\\car_price.csv')

df1=df.drop('Car_Name',axis=1)

Encoder=OneHotEncoder(drop='first')

df_Cat=Encoder.fit_transform(df1.loc[:,['Fuel_Type','Seller_Type','Transmission']])


cat_col=['Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual','Transmission_Manual']

df2=df1.select_dtypes('number').join(pd.DataFrame(df_Cat.toarray() ,columns=cat_col))

y=df2.loc[:,'Selling_Price']

X=df2.drop('Selling_Price',axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

RFR=RandomForestRegressor(max_depth=5)

RFR_model=RFR.fit(X_train,y_train)

file = open('RFR_model.pickle','wb')
pickle.dump(RFR_model, file)
file.close()

file = open('Encoder.pickle','wb')
pickle.dump(Encoder, file)
file.close()






