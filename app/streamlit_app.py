import streamlit as st
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "social_media_addiction_app_model.pkl"
)

model = joblib.load(MODEL_PATH)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "label_encoders.pkl"
)

encoders = joblib.load(ENCODER_PATH)

print(type(encoders))
print(encoders)
print(type(model))

st.write("Model Loaded Successfully ✅")


st.set_page_config(
    page_title="Social Media Addiction Predictor",
    page_icon="📱"
)

st.title("📱 Student Social Media Addiction Risk Predictor")

st.write(
    "Predict the addiction risk level of a student based on social media behavior."
)

# Inputs
age = st.number_input(
    "Age",
    min_value=15,
    max_value=35,
    value=20
)

usage_hours = st.number_input(
    "Average Daily Usage Hours",
    min_value=0.0,
    max_value=15.0,
    value=5.0
)

sleep_hours = st.number_input(
    "Sleep Hours Per Night",
    min_value=1.0,
    max_value=12.0,
    value=7.0
)

mental_health = st.slider(
    "Mental Health Score",
    1,
    10,
    7
)

conflicts = st.slider(
    "Conflicts Over Social Media",
    0,
    10,
    3
)

# Feature Engineering
usage_sleep_ratio = usage_hours / sleep_hours

wellbeing_score = sleep_hours + mental_health

if conflicts <= 3:
    conflict_intensity = 1
elif conflicts <= 6:
    conflict_intensity = 2
else:
    conflict_intensity = 3

# Prediction Button
if st.button("Predict Risk"):

    # Feature Engineering
    usage_sleep_ratio = usage_hours / sleep_hours

    wellbeing_score = sleep_hours + mental_health

    if conflicts <= 3:
        conflict_intensity = 0
    elif conflicts <= 6:
        conflict_intensity = 1
    else:
        conflict_intensity = 2

    input_data = pd.DataFrame({
        "Age": [age],
        "Avg_Daily_Usage_Hours": [usage_hours],
        "Sleep_Hours_Per_Night": [sleep_hours],
        "Mental_Health_Score": [mental_health],
        "Conflicts_Over_Social_Media": [conflicts],
        "Usage_Sleep_Ratio": [usage_sleep_ratio],
        "Wellbeing_Score": [wellbeing_score],
        "Conflict_Intensity": [conflict_intensity]
    })

    prediction = model.predict(input_data)[0]

    risk_map = {
        0: "Low Risk 🟢",
        1: "Medium Risk 🟡",
        2: "High Risk 🔴"
    }

    st.subheader("Prediction Result")
    if prediction == 0:
        st.success("Low Risk 🟢")

    elif prediction == 1:
        st.warning("Medium Risk 🟡")

    else:
        st.error("High Risk 🔴")

    probabilities = model.predict_proba(input_data)[0]

    confidence = max(probabilities) * 100

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    st.subheader("Input Summary")

    st.write(input_data)

    # Recommendations
    if prediction == 0:
        st.info(
            "Healthy social media usage pattern. Continue maintaining balance."
        )

    elif prediction == 1:
        st.warning(
            "Moderate addiction risk. Consider reducing screen time and improving sleep habits."
        )

    else:
        st.error(
            "High addiction risk detected. Reduce daily usage, improve sleep quality, and prioritize mental well-being."
        )
    
    st.markdown("---")
    st.markdown(
        "Developed by Vedika Kirve | Data Science Project"
)