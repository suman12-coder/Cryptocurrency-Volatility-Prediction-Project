 # Machine Learning Pipeline – Cryptocurrency Volatility Prediction
 ---

##  Data Pipeline
**Input → Processing → Output**

-  **Data Loading:** Load CSV dataset
- **Data Cleaning** Handle NaNs, duplicates, outliers
- **Feature Engineering:** Add volatility & return features
- **Scaling:**  Normalize numeric columns 
- **Splitting:** Train-Test split (70-30)

---

##  Modeling Pipeline
1. Train Base Random Forest Model  
2. Evaluate using MAE, R²  
3. Perform GridSearchCV for hyperparameter tuning  
4. Train best model  
5. Save scaler, model, metadata as `.pkl`  

---

## Deployment Pipeline

- **Web App** Streamlit 
- **Hosting** GitHub + Streamlit Cloud 
- **Files Used**  `app.py`, `rf_vol_model.pkl`, `scaler.pkl`, `model_meta.pkl`, `requirements.txt` 

---

##  End-to-End Flow
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Save → Streamlit Deployment → User Prediction

**Final output**: Predicted volatility displayed on Streamlit web app.
