## HLD.md (High-Level Design)- Cryptocurrency Volatility Prediction
---
# Objective:
Build a machine learning model to predict the **next-day price volatility** of cryptocurrencies using market features like price, volume, and market cap.
---

## 2. System Architecture

**Architecture Flow:**
1. **Data Collection** → Historical crypto price data (CSV)
2. **Data Preprocessing** → Cleaning, feature engineering
3. **EDA** → Visualization & insights
4. **Modeling** → Random Forest Regressor (base and tuned)
5. **Evaluation** → MAE, RMSE, and R² metrics
6. **Deployment** → Streamlit app + GitHub hosting

---

#  Components
- **Data Source:** CSV of crypto historical data
- **Model:** RandomForestRegressor from Scikit-learn
- **Scaler:** MinMaxScaler
- **Evaluation:** MAE, R²
- **Deployment:** Streamlit Cloud
- **Version Control:** GitHub

---

##  Tools and Technologies
- **Language:**  Python
- **Libraries:** pandas, numpy, sklearn, matplotlib, seaborn, streamlit
- **Deployment:** Streamlit Cloud
- **IDEs:** Jupyter Lab 

---

##  Model Inputs & Output
- **Inputs:** `open`, `high`, `low`, `close`, `volume`, `marketCap`, derived features  
- **Output:** Predicted next-day volatility (continuous value)

---

##  Advantages
- Easy interpretability  
- Efficient performance  
- Simple web interface  
- Scalable deployment via Streamlit  

---
