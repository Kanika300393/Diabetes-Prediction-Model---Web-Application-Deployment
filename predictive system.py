# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import  pickle

#lading the saved model
loaded_model = pickle.load(open('C:/Users/kanik/OneDrive/Desktop/Python Code/Machine Learning Projects/Diabetes/trained_model.sav','rb')) #rb reading binary

#trying with loaded_model
input_data =(1,103,30,38,83,43.3,0.183,33)

#changing the imput data to numpy array

input_data_as_numpy_array = np.asarray(input_data)

#reshape the array as we predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print('The person is not Diabetic')
else:
    print('The person is Diabetic')