import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("rf_vol_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
metadata = pickle.load(open("model_meta.pkl", "rb"))

st.set_page_config(page_title="Crypto Volatility Predictor", page_icon="💹")
st.title("💹 Cryptocurrency Volatility Prediction")
st.write("This app predicts next-day volatility using a trained Random Forest model.")

# Get feature names from metadata
features = metadata["features"]

# Create inputs
st.sidebar.header("Input Features")
inputs = []
for feat in features:
    val = st.sidebar.number_input(f"{feat}", value=0.0)
    inputs.append(val)

if st.sidebar.button("Predict Volatility"):
    # Create DataFrame
    data = pd.DataFrame([inputs], columns=features)
    # Scale data
    data_scaled = scaler.transform(data)
    # Predict
    pred = model.predict(data_scaled)[0]
    st.success(f"Predicted Next-Day Volatility: **{pred:.5f}**")
