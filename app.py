import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("wine_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🍷 Wine Quality Prediction App")

st.write("Enter wine properties:")

# Inputs
fixed_acidity = st.number_input("Fixed Acidity")
volatile_acidity = st.number_input("Volatile Acidity")
citric_acid = st.number_input("Citric Acid")
residual_sugar = st.number_input("Residual Sugar")
chlorides = st.number_input("Chlorides")
free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide")
total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide")
density = st.number_input("Density")
pH = st.number_input("pH")
sulphates = st.number_input("Sulphates")
alcohol = st.number_input("Alcohol")

if st.button("Predict Quality"):

    # ✅ FIX: Use DataFrame with correct column names
    features = pd.DataFrame([{
        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol
    }])

    # Scale
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    # Output
    if prediction == 1:
        st.success(f"GOOD Quality 🍷 (Confidence: {prob:.2f})")
    else:
        st.error(f"BAD Quality ❌ (Confidence: {prob:.2f})")