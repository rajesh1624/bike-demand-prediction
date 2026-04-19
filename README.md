# 🚴 Bike Demand Prediction (End-to-End ML Project)

## 📌 Overview

This project builds an end-to-end machine learning system to predict daily bike rental demand based on environmental and seasonal factors.

The pipeline includes:

* Data analysis (EDA)
* Feature engineering
* Model building
* Model evaluation
* API development (FastAPI)
* Frontend UI (Streamlit)

---

## 🎯 Problem Statement

Bike-sharing systems generate large amounts of data influenced by weather, seasonality, and time. Predicting demand helps optimize operations and improve user experience.

---

## 🎯 Objective

* Analyze factors affecting bike demand
* Identify important features
* Build a predictive model
* Deploy using API + UI

---

## 💼 Business Use Case

This system helps:

* Optimize bike availability
* Improve customer satisfaction
* Reduce operational costs
* Enable data-driven decision making

---

## 🧠 Features Used

* season
* yr
* mnth
* holiday
* weekday
* workingday
* weathersit
* temp
* hum
* windspeed

---

## ⚙️ Model Used

* Linear Regression (baseline model)
* Focus on interpretability and simplicity

---

## 📊 Model Evaluation

* R² Score ≈ 0.84
* RMSE ≈ 800 bikes

👉 The model explains ~84% of variance with reasonable prediction error.

---

## ⚠️ Limitation

Linear Regression can produce negative predictions.

✔ Solution:

```python
prediction = max(0, int(result))
```

---

## 🚀 Project Architecture

```
User Input (Streamlit)
        ↓
FastAPI API (/predict)
        ↓
Trained Model (.pkl)
        ↓
Prediction Output
        ↓
Displayed in UI
```

---

## 🖥️ How to Run

### 1. Create Virtual Environment

```bash
uv venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 3. Run API

```bash
uvicorn src.api:app --reload
```

### 4. Run Streamlit

```bash
streamlit run app.py
```

---

## 🧪 Example Test

* Bad weather → low demand
* Good weather → high demand

✔ Model behaves logically based on real-world patterns.

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Hyperparameter tuning
* Better feature engineering

---

## 📌 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Streamlit

---

## 👤 Author

Rajesh Chauhan
