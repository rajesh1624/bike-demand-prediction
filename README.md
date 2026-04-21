# 🚴 Bike Demand Prediction (End-to-End ML System)

## 📌 Overview

This project builds and deploys a **production-ready machine learning system** to predict daily bike rental demand based on weather, seasonal, and temporal features.

The system includes:

* Data analysis (EDA)
* Feature engineering
* Model training
* REST API development using FastAPI (POST /predict endpoint for model inference)
* Interactive UI using Streamlit
* Cloud deployment using Render

---

## 🌐 Live Demo (🔥)

👉 **Streamlit UI:**
https://bike-demand-ui.onrender.com

👉 **FastAPI Docs:**
https://bike-demand-api.onrender.com/docs

---

## 🎯 Problem Statement

Bike-sharing demand fluctuates due to environmental and seasonal factors. Accurate prediction helps optimize fleet availability and improve operational efficiency.

---

## 💼 Business Use Case

* Optimize bike distribution
* Reduce shortages and over-supply
* Improve customer satisfaction
* Enable data-driven planning

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
* Chosen for simplicity and interpretability

---

## 📊 Model Performance

* R² Score ≈ 0.84
* RMSE ≈ 800 bikes

👉 Model explains ~84% variance in demand.

---

## ⚠️ Limitation

Linear regression may produce negative predictions.

✔ Fix applied:

```
prediction = max(0, int(result))
```

---

## 🏗️ System Architecture

```
User (Streamlit UI)
        ↓
FastAPI (/predict endpoint)
        ↓
Trained ML Model (.pkl)
        ↓
Prediction Response
        ↓
Displayed in UI
```

---

## ⚡ Deployment Architecture

* Backend deployed on **Render (FastAPI)**
* Frontend deployed on **Render (Streamlit)**
* Communication via REST API

---

## 🧪 Example

* Clear weather + working day → High demand
* Rainy weather → Low demand

✔ Model reflects real-world patterns.

---

## 🚀 How to Run Locally

```
pip install -r requirements.txt
```

### Run API

```
uvicorn src.api:app --reload
```

### Run UI

```
streamlit run app.py
```

---

## 🔥 Key Learnings

* Built full ML pipeline (data → model → API → UI)
* Deployed ML system on cloud (Render)
* Handled API-UI integration issues
* Debugged real-world errors:

  * JSONDecodeError
  * Deployment failures
  * Dependency issues
* Understood production-level architecture

---

## 🔮 Future Improvements

* Use advanced models (XGBoost, Random Forest)
* Add model monitoring
* Improve UI/UX
* Add Docker containerization

---

## 📌 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* FastAPI
* Streamlit
* Render (Cloud Deployment)

---

## 👤 Author

**Rajesh Chauhan**
