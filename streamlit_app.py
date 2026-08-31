import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(page_title="Student Health Risk Predictor", page_icon="🩺")
st.title("🩺 Student Health Risk Predictor")
st.write("Enter details to predict health risk category.")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        sleep_duration = st.number_input("Sleep Duration (hrs)", value=None, placeholder="e.g. 7.5")
        heart_rate = st.number_input("Heart Rate (bpm)", value=None, placeholder="e.g. 75")
        bmi = st.number_input("BMI", value=None, placeholder="e.g. 22.5")
        calorie_expenditure = st.number_input("Calorie Expenditure", value=None, placeholder="e.g. 2000")
        step_count = st.number_input("Step Count", value=None, placeholder="e.g. 8000")
        exercise_duration = st.number_input("Exercise Duration (min)", value=None, placeholder="e.g. 30")
        water_intake = st.number_input("Water Intake (L)", value=None, placeholder="e.g. 2.0")

    with col2:
        diet_type = st.selectbox("Diet Type", ["veg", "non-veg", "balanced"], index=None, placeholder="Select...")
        stress_level = st.selectbox("Stress Level", ["low", "medium", "high"], index=None, placeholder="Select...")
        sleep_quality = st.selectbox("Sleep Quality", ["poor", "average", "good"], index=None, placeholder="Select...")
        physical_activity_level = st.selectbox("Physical Activity", ["sedentary", "moderate", "active"], index=None, placeholder="Select...")
        smoking_alcohol = st.selectbox("Smoking/Alcohol", ["no", "occasional", "yes"], index=None, placeholder="Select...")
        gender = st.selectbox("Gender", ["male", "female", "other"], index=None, placeholder="Select...")

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "sleep_duration": sleep_duration,
        "heart_rate": heart_rate,
        "bmi": bmi,
        "calorie_expenditure": calorie_expenditure,
        "step_count": step_count,
        "exercise_duration": exercise_duration,
        "water_intake": water_intake,
        "diet_type": diet_type,
        "stress_level": stress_level,
        "sleep_quality": sleep_quality,
        "physical_activity_level": physical_activity_level,
        "smoking_alcohol": smoking_alcohol,
        "gender": gender,
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        st.success(f"Predicted: **{result['health_condition']}**")
        st.bar_chart(result["probabilities"])
    except requests.exceptions.RequestException as exc:
        st.error(f"Prediction request failed: {exc}")
        st.caption("Make sure the FastAPI backend is running at http://127.0.0.1:8000")