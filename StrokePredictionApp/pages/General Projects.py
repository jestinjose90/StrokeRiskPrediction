import streamlit as st
import runpy
import os

st.title("General Projects")

project_options = ["Select Project","Stroke Risk Prediction App"]

main_choice = st.selectbox("Choose a project",project_options,index=0)

if main_choice == "Stroke Risk Prediction App":
        choice = st.selectbox("Choose an option:", ["Home","Application","Performance Metrics", "SHAP Modeling"])
        st.markdown("<br>", unsafe_allow_html=True) 
        if choice == "Home":
                runpy.run_path(os.path.join("modules", "Home.py"))
        elif choice == "Application":
                runpy.run_path(os.path.join("modules", "Application.py"))
        elif choice == "Performance Metrics":
                runpy.run_path(os.path.join("modules", "performance_metrics.py"))
        elif choice == "SHAP Modeling":
            runpy.run_path(os.path.join("modules", "shap_modeling.py"))
        else:
               st.error("Page not Found")

