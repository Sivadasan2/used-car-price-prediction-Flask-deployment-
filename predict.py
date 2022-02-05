# predict.py

# Importing the Libraries
import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

# Reading the Model Pickle object file
file = open('RFR_model.pickle', 'rb')
RF_model = pickle.load(file)
file.close()


# Reading the Transformer object file

file2 = open('Encoder.pickle', 'rb')
Encoder = pickle.load(file2)
file2.close()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    x=[]
    col=['Year','Present_Price', 'Kms_Driven', 'Fuel_Type','Seller_Type', 'Transmission', 'Owner']    
    x= [i for i in request.form.values()]    
    x_val=pd.DataFrame([x],columns=col)   
    
    for i in x_val.columns:
        if i in ['Fuel_Type','Seller_Type','Transmission']:
            x_val[i]=x_val[i].astype('object')
            
        elif i in ['Present_Price','Kms_Driven']:
            x_val[i]=x_val[i].astype('float')
        else:
            x_val[i]=x_val[i].astype('int64')          
            
            
    
    x_val_cat=Encoder.transform(x_val.select_dtypes(exclude='number'))
    cat_col=['Fuel_Type_Diesel', 'Fuel_Type_Petrol', 'Seller_Type_Individual','Transmission_Manual']
    x_val=x_val.select_dtypes('number').join(pd.DataFrame(x_val_cat.toarray() ,columns=cat_col))
    y_pred=RF_model.predict(x_val)   
    output=round(y_pred[0],2)
    return render_template('index.html', prediction_text='Predicted car price should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)














