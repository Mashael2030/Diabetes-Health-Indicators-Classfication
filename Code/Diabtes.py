# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle
import numpy as np
import pandas as pd

data=pickle.load(open('saved_steps.pkl','rb'))

model = data['model']
scaler= data['scaler']
columns = ['HighBP', 'HighChol', 'BMI', 'HeartDiseaseorAttack','PhysActivity', 'GenHlth','MentHlth','DiffWalk', 'Age']      
                   
def predict_fareamount(HighBP, HighChol, BMI, HeartDiseaseorAttack,PhysActivity,GenHlth,MentHlth,DiffWalk,Age):
    input=np.array([[HighBP, HighChol, BMI, HeartDiseaseorAttack,PhysActivity,GenHlth,MentHlth,DiffWalk,Age]]).astype(np.float64)
    input=pd.DataFrame(scaler.transform(input), columns=columns)
    prediction=model.predict(input)
    return int(prediction)
def main():
    
    st.title(" Diabetes Health Indicators  ")
    Age = st.number_input("Age :")
    BMI = st.number_input("BMI : ")
    GenHlth = st.number_input("GenHlth :")
    HighBP = st.number_input("HighBP : ")
    HeartDiseaseorAttack = st.number_input(" HeartDiseaseorAttack :")
    PhysActivity = st.number_input("PhysActivity : ")
    MentHlth = st.number_input("MentHlth : ")
    DiffWalk= st.number_input("DiffWalk: ")
    HighChol= st.number_input("HighChol : ")
    
    
    
    
  
    if st.button("Predict"):      
        output=predict_fareamount(HighBP, HighChol, BMI, HeartDiseaseorAttack,PhysActivity,GenHlth,MentHlth,DiffWalk,Age)
        st.write('Diebtes  ', output)
if __name__=='__main__':
    main()

