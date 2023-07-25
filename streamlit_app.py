# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:01:13 2023

@author: Aaron Mobley
"""

import streamlit as st
import numpy as np
import joblib

#Interface for streamlit 

st.markdown('## Breast Cancer Survival Prediction')

Age = st.number_input('Age')

GenderR = st.number_input('Gender Male = 0 Female = 1')

Protein4 = st.number_input('Protein')

Tumour_StageR = st.number_input('Tumour Stage')

HistologyR = st.number_input('Histology (Type)')

#Analyze button

if st.button('Analyze'):
    model = joblib.load('cancer_model.pkl')
    x = np.array([Age, GenderR, Protein4, Tumour_StageR, HistologyR])
    if any( x <= 0):
        st.markdown('## Inputs must be greater than 0')
    else:
        st.markdown(f'### Prediction is {model.predict([[Patient_Status]])[0]}')