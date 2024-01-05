# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 07:01:06 2023

@author: Sanvidha
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Sanvidha/Desktop/Multiple_disease/MULTIPLE DISEASE PREDICTION MODEL/trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/Sanvidha/Desktop/Multiple_disease/MULTIPLE DISEASE PREDICTION MODEL/trained_modelh.sav', 'rb'))

parkinson_model = pickle.load(open('C:/Users/Sanvidha/Desktop/Multiple_disease/MULTIPLE DISEASE PREDICTION MODEL/trained_modelp.sav', 'rb'))


with st.sidebar:
    
    selected = option_menu('Sanvidhas Multiple Disease Prediction Model', 
                           
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkisons Disease Prediction'],
                          
                          icons=['activity','heart','person'],
                          
                          default_index= 0)
    
#diabetes prediction page 
if (selected == 'Diabetes Prediction'):
    
    st.title('S. Diabetes Prediction')
    
    
    
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
    
        diagnosis = diabetes_model.predict([[Pregnancies,  Glucose, BloodPressure,  SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diagnosis [0] == 1):
            diagnosis = 'The person is diabetic'
        
        else:
            diagnosis = 'The person is not diabetic'
    st.success(diagnosis)
    
if (selected == 'Heart Disease Prediction'):
    
    st.title('S. Heart Disease Prediction ')
    
    
    
    age = st.text_input('Enter the age of the patient')
    Sex = st.text_input('Enter the sex of the Patient')
    cp = st.text_input('Enter chest pain type of the patient')
    trestbps = st.text_input('Enter the resting blood pressure of the patient')
    chol = st.text_input('Enter the Serum Cholesterol Level of the patient')
    fbs = st.text_input('Enter the Fasting Blood Sugar of the patient')
    thalach = st.text_input('Enter the resting electrocardiographic result value of the patient')
    exang = st.text_input('Enter the exercise induced angina of the patient')
    oldpeak = st.text_input('Enter the old peak of the patient')
    slope = st.text_input('Enter the slope of the patient')
    ca = st.text_input('Enter the number of major blood vessels colored by flurosopy of the patient')
    thal = st.text_input('Enter the thal of the patient')
    
    diagnosis = ''
    
    if st.button(' Heart Test Result'):
    
        diagnosis = heart_disease_model.predict([[age, Sex, cp,  trestbps, chol, fbs, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (diagnosis [0] == 1):
            diagnosis = 'The person has heart disease'
        
        else:
            diagnosis = 'The person does not have heart disease'
    st.success(diagnosis)
    
    

if (selected == 'Parkisons Disease Prediction'):
    
    st.title('S. Parkisons Disease')
    
    name = st.text_input('Enter the name of the patient')
    Fo = st.text_input('Enter the Average vocal fundamental frequency of the Patient')
    Fhi = st.text_input('Enter Maximum vocal fundamental frequency of the patient')
    Flo = st.text_input('Enter Minimum vocal fundamental frequencyof the patient')
    Jitter = st.text_input('Enter the Jitter percentage of the patient')
    Jitter_abs= st.text_input('Enter the Jitter abs of the patient')
    RAP = st.text_input('Enter the RAP of the patient')
    PPQ = st.text_input('Enter the PPQ of the patient')
    Jitter_DDP = st.text_input('Enter the Jitter DDP of the patient')
    MDVP_Shimmer= st.text_input('Enter the MDVP Shimmer of the patient')
    MDVP_Shimmer_dB = st.text_input('Enter the MDVP Shimmer in dB of the patient')
    Shimmer_APQ3 = st.text_input('Enter the Shimmer APQ3 of the patient')
    Shimmer_APQ5 = st.text_input('Enter the Shimmer APQ5 of the patient')
    MDVP_APQ = st.text_input('Enter the MDVP APQ of the patient')
    Shimmer_DDA = st.text_input('Enter the Shimmer DDA of the patient')
    NHR = st.text_input('Enter the NHR of the patient')
    RHN = st.text_input('Enter the RHN of the patient')
    RPDE = st.text_input('Enter the RPDE of the patient')
    DFA = st.text_input('Enter the DFA of the patient')
    spread1 = st.text_input('Enter the spread 1 of the patient')
    spread2 = st.text_input('Enter the spread 2 of the patient')
    D2 = st.text_input('Enter the D2 of the patient')
    PPE = st.text_input('Enter the PPE of the patient')
    
    
    diagnosis = ''
    
    if st.button(' Parkinsons Test Result'):
    
        diagnosis = parkinson_model.predict([[name,Fo, Fhi , Flo, Jitter, Jitter_abs, RAP, PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if (diagnosis [0] == 1):
            diagnosis = 'The person has Perkinsons disease'
        
        else:
            diagnosis = 'The person does not have Perkinsons disease'
    st.success(diagnosis)

