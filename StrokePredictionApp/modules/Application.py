import numpy as np
import joblib
import streamlit as st
import pandas as pd



# Load trained model
model_pipeline = joblib.load('stroke_model_sklearn.pkl')


# Collect user input
gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
age = st.slider("Age", 0, 100, 30)
hypertension = st.selectbox("Hypertension", [0, 1])
heart_disease = st.selectbox("Heart Disease", [0, 1])
ever_married = st.selectbox("Ever Married", ['Yes', 'No'])
work_type = st.selectbox("Work Type", ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
avg_glucose_level = st.slider("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.slider("BMI", 10.0, 60.0, 22.0)
smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

user_input_df = pd.DataFrame([{
        'gender': gender,
        'age': age,
        'hypertension': hypertension,
        'heart_disease': heart_disease,
        'ever_married': ever_married,
        'work_type': work_type,
        'Residence_type': residence_type,
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'smoking_status': smoking_status
    }])

if st.button("Predict Stroke Risk"):
        prediction = model_pipeline.predict(user_input_df)[0]

        if prediction == 1:
            st.error("High Risk of Stroke")  # red colored message
        else:
            st.success("Low Risk of Stroke")  # green colored message

