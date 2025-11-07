import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("rf_vol_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
metadata = pickle.load(open("model_meta.pkl", "rb"))

st.set_page_config(page_title="Crypto Volatility Predictor")
st.title("Cryptocurrency Volatility Prediction")
st.write("This app predicts next-day volatility using a trained Random Forest model.")

features = metadata["features"]

st.sidebar.header("Input Features")
inputs = []
for feat in features:
    val = st.sidebar.number_input(f"{feat}", value=0.0)
    inputs.append(val)

if st.sidebar.button("Predict Volatility"):
    data = pd.DataFrame([inputs], columns=features)
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)[0]
    st.success(f"Predicted Next-Day Volatility: **{pred:.5f}**")
