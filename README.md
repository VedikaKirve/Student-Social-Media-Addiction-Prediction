# Student Social Media Addiction Risk Predictor

## Project Overview
A Machine Learning project that predicts a student's social media addiction risk level based on usage patterns, sleep habits, mental health, and social conflicts.

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn

## Workflow
Data Cleaning → EDA → Feature Engineering → Model Building → Evaluation → Deployment

## Features
- Predicts addiction risk
- Confidence score
- Personalized recommendations
- Interactive Streamlit dashboard

## Project Structure
Student-Social-Media-Addiction-Prediction/
│
├── app/
│   └── streamlit_app.py
|
├── assets/
│   ├── home_page.png
│   ├── prediction_result.png
│   ├── correlation_heatmap.png
│   └── feature_importance.png
│
├── data/
│   ├── processed/
│   │   └── cleaned_data.csv
|   |   └──featured_data.csv
│   │
│   └── raw/
│       └── Students Social Media Addiction.csv
│
├── models/
│   ├── label_encoders.pkl
│   ├── social_media_addiction_app_model.pkl
│   └── social_media_addiction_model.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_building.ipynb
│   └── 05_model_evaluation.ipynb
│
├── reports/
│   └── project_summary.pdf
|
|── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── predict.py
│   └── train_model.py
│
├── .gitignore
├── README.md
└── requirements.txt

## 🌍 Live Demo
https://student-social-media-addiction-prediction-tqg5zkfddpqzsnvpq8ab.streamlit.app/
