# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 13:25:10 2024

@author: kanik
"""

import numpy as np
import pickle
import streamlit as st

#lading the saved model

loaded_model = pickle.load(open('C:/Users/kanik/OneDrive/Desktop/Python Code/Machine Learning Projects/Diabetes/trained_model.sav','rb')) #rb reading binary

#creating a function for prediction

def diabeties_prediction(input_data):
    

    #changing the imput data to numpy array

    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==0):
        return'The person is not Diabetic'
    else:
        return'The person is Diabetic'
        
        
def main():
    
    #giving title
    st.title('Diabetes Prediction Web App')
    
    #getting the imput data from user
    
    
    Pregnancies = st.text_input('Number of Pregnencies')
    Glucose = st.text_input('Gulucose Level')
    BloodPressure = st.text_input('BP Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree Function Value')
    Age = st.text_input('Age of person')
    
    
    #code for prediction
    diagnose = ''
    
    #create a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnose= diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnose)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    