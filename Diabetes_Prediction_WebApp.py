# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Computer Sanvidha Haribhakta/ML/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_array = np.asarray(input_data)
    input_reshaped = input_data_as_array.reshape(1, -1)


    prediction = loaded_model.predict(input_reshaped )
    print(prediction)

    if (prediction [0] == 0):
      print('The person is not diabetic')
    else:
      print('The person is diabetic')

def main():
    
    #Title
    st.title('Diabetes Prediction web App')
    
    Pregnancies= st.text_input('Enter Number of Pregnancies of the patient')
    Glucose= st.text_input('Enter Glucose level of the Patient')
    BloodPressure = st.text_input('Enter Blood pressure of the patient')
    SkinThickness = st.text_input('Enter the Skin Thickness of the patient')
    Insulin = st.text_input('Enter the Insulin Level of the patient')
    BMI = st.text_input('Enter the BMI of the patient')
    DiabetesPedigreeFunction= st.text_input('Enter the Diabetes Pedigree Function of the patient')
    Age= st.text_input('Enter the age of the patient')
    
    
    diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,  Glucose, BloodPressure,  SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()