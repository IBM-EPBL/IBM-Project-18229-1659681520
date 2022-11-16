# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:38:30 2022

@author: home
"""
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle as p
app=Flask(__name__)
model=p.load(open('CKD.pk1','rb'))
@app.route('/')
def HOME():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def prediction():    
    form_value=request.form.values()    
    data=[]
    for x in form_value:
        data.append(pd.to_numeric(x).astype(float))
    features_value=[np.array(data)]  
    features_name=['age','blood_urea','blood glucose random','coronary_artery_disease',
                   'anemia','pus_cell','red_blood_cell','diabetesmellitus','pedal_edema']
    df=pd.DataFrame(features_value, columns=features_name)
    
    output=model.predict(df)
    if(output==0):
        return render_template('index.html' , pred='Oops!! You have Kidney Chronic Disease. So, please concern a Doctor')
    else:
        return render_template('index.html' , pred='you are not affected by Chronic kidney Disease')

if __name__=='__main__':
    app.run(debug=True)


