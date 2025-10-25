import streamlit as st

st.header("Stroke Risk Prediction")
st.image("images/stroke-img.png",width=550)


# Project Overview
st.markdown("""
## Project Overview

The purpose of this page is to provide a clear, non-technical overview of:

- The problem we aim to solve
- The approach we used
- The results we achieved


---
""")

# Problem
st.subheader("The Problem")
st.markdown("""
Stroke is a medical emergency that can lead to permanent disability or death. Early detection and risk assessment are crucial.

However, many people at risk of stroke are unaware of it until symptoms appear. This project aims to provide a quick, data-driven stroke risk prediction app  to raise awareness and encourage proactive health monitoring.
""")

# Approach
st.subheader(" The Approach")
st.markdown("""
We collected health-related data , trained and tested 7 different ML models and selected best performing model  to identify stroke risk patterns. The goal was to find a model that does'nt miss any stroke
stroke cases, while also being as accurate and reliable as possible. The data includes:

- Age
- Hypertension and heart disease history
- Average glucose level
- Body Mass Index (BMI)
- Smoking status
- Gender
- Marital Status , type of work and Residence Type

After careful testing we selected **XGBoost model** because it did the best job of detecting stroke risks without making too many false alarms. SHAP (SHapley Additive exPlanations) values were used to explain the model's decisions.
""")

# Results
st.subheader("Results")
st.markdown("""
The model was evaluated on test data with the following outcomes:

- **Accuracy**: 87%
- **Precision**: 80%
- **Recall**: 84%

These results indicate that the model is effective at identifying individuals at risk.
""")

