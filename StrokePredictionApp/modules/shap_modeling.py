import streamlit as st
from PIL import Image
import os

    #Title
st.title("SHAP Summary Plot")
image_path = "images/Shap.png"
image = Image.open(image_path)
st.image(image,width=550)

st.markdown(""" 
            The SHAP plot reveals that age, average glucose level, BMI, hypertension, and heart disease are the top contributors to the model’s stroke predictions. 
            Higher values of these features generally increase predicted stroke risk. 
            Importantly, these findings align closely with established medical research, which identifies these factors as major stroke risk determinants. 
            This overlap between model insights and clinical evidence increases confidence in the model’s relevance for real-world health risk assessment
            
            """)