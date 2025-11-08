#  Final Project Report – Cryptocurrency Volatility Prediction

##  Project Overview
This project predicts next-day volatility in cryptocurrency prices using Random Forest Regression based on historical market data.

---

##  Objectives
- Analyze crypto price movements and patterns  
- Create new predictive features (returns, volatility, etc.)  
- Build and tune Random Forest model for volatility prediction  
- Deploy model as a Streamlit web application  

---
# Methodology
 - Data Cleaning and Preprocessing
 - Feature Engineering (volatility, moving averages, liquidity ratio)
 - Model Training using Random Forest
 - Evaluation with MAE,and R²
  - Deployment using Streamlit interface

### Data Preparation
- Loaded CSV with open, high, low, close, volume, marketCap  
- Cleaned missing and duplicate records  
- Derived new variables for volatility and daily returns  
- Normalized numeric data with MinMaxScaler  

### EDA Insights
- Strong correlation between price features  
- High market volatility during trading surges  
- Distinct patterns across cryptocurrencies  

---

## 4. Model Training and Evaluation
**Base Random Forest**
  - MAE :0.015 , R2 Score:0.64 
  - Stable and accurate 
**Tuned Random Forest Model** 
 - MAE :0.018 , R2 Score: 0.59
 -  More generalized |


# Best parameters from tuning:
- {'max_depth': 5, 'min_samples_split': 2, 'min_samples_leaf': 1, 'n_estimators': 200}

# Deployment
- Used **Streamlit** for front-end  
- Hosted via **Streamlit Cloud**  
- Model and scaler stored as `.pkl`  
- Inputs taken via sidebar; outputs displayed dynamically  

---

##  Results & Conclusion
- Model predicts next-day crypto volatility with reasonable accuracy (R² ≈ 0.6)  
- Volatility largely depends on `open`, `close`, `high`, and `low` prices  
- Deployment successfully provides real-time prediction interface  

