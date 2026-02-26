from Src.Stress_Level.Logging import logging
from Src.Stress_Level.Exception import Cu_Exception
import sys
import pickle
import os
import pandas as pd
import streamlit as st

if __name__=="__main__":
    try:

        with open("artifacts/Data_Preprocessing.pkl", "rb") as f:
            preprocessor = pickle.load(f)

        with open("artifacts/model.pkl", "rb") as file:
            model = pickle.load(file)

        st.title(" Stress Level Prediction" )

        st.markdown(" Enter Your Details Below")


        age = st.number_input("Age", min_value=10, max_value=100, step=1)

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        occupation = st.selectbox(
            "Occupation",
            ["Professional", "Student", "Business Owner", "Freelancer"]
        )

        device_type = st.selectbox(
            "Device Type",
            ["Android", "iOS"]
        )

        daily_phone_hours = st.number_input("Daily Phone Hours", min_value=0.0,step=0.5)
        social_media_hours = st.number_input("Social Media Hours", min_value=0.0,step=0.5)
        work_productivity_score = st.number_input("Work Productivity Score (0-10)", min_value=0.0, max_value=10.0,step=1.0)
        sleep_hours = st.number_input("Sleep Hours", min_value=0.0,step=0.5)
        caffeine_intake = st.number_input("Caffeine Intake (Cups)", min_value=0.0,step=1.0)
        app_usage_count = st.number_input("App Usage Count", min_value=0)
        weekend_screen_time = st.number_input("Weekend Screen Time Hours", min_value=0.0,step=0.5)


        if st.button("Predict Stress Level"):

            data = {
                "Age": [age],
                "Gender": [gender],
                "Occupation": [occupation],
                "Device_Type": [device_type],
                "Daily_Phone_Hours": [daily_phone_hours],
                "Social_Media_Hours": [social_media_hours],
                "Work_Productivity_Score": [work_productivity_score],
                "Sleep_Hours": [sleep_hours],
                "Caffeine_Intake_Cups": [caffeine_intake],
                "App_Usage_Count": [app_usage_count],
                "Weekend_Screen_Time_Hours": [weekend_screen_time]
            }

            df = pd.DataFrame(data)

    
            transformed_data = preprocessor.transform(df)

            prediction = model.predict(transformed_data)

            pred_value = prediction[0]

            if pred_value < 4:
                res = "Less Stress"
            elif 4 <= pred_value < 6.5:
                res = "Medium Stress"
            else:
                res = "High Stress"

            st.success(f"Predicted Stress Level: {res}")

        

    except(Exception) as e:
        raise Cu_Exception(e,sys)
