import streamlit as st
import requests

API_URL = "https://bike-demand-api.onrender.com/predict"

st.title("🚴 Bike Demand Prediction App")

st.markdown("""
This app predicts daily bike rental demand based on weather and seasonal conditions.
👉 Select the inputs and click **Predict**
""")

st.subheader("📊 Input Features")

# -------- Season --------
season_dict = {
    "Spring 🌸": 1,
    "Summer ☀️": 2,
    "Fall 🍂": 3,
    "Winter ❄️": 4
}
season_label = st.selectbox("Season", list(season_dict.keys()))
season = season_dict[season_label]

# -------- Month --------
mnth = st.selectbox("Month", list(range(1, 13)))

# -------- Weekday --------
weekday_dict = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6
}
weekday_label = st.selectbox("Weekday", list(weekday_dict.keys()))
weekday = weekday_dict[weekday_label]

# -------- Weather --------
weather_dict = {
    "Clear 🌤️": 1,
    "Mist 🌫️": 2,
    "Light Rain 🌧️": 3
}
weathersit_label = st.selectbox("Weather Situation", list(weather_dict.keys()))
weathersit = weather_dict[weathersit_label]

# -------- Sliders --------
temp = st.slider("Temperature (Normalized)", 0.0, 1.0, 0.5)
hum = st.slider("Humidity (Normalized)", 0.0, 1.0, 0.5)
windspeed = st.slider("Windspeed (Normalized)", 0.0, 1.0, 0.2)

# -------- Year --------
year_dict = {
    "2011": 0,
    "2012": 1
}
yr_label = st.selectbox("Year", list(year_dict.keys()))
yr = year_dict[yr_label]

# -------- Binary Inputs --------
holiday = st.selectbox("Holiday (0 = No, 1 = Yes)", [0, 1])
workingday = st.selectbox("Working Day (0 = No, 1 = Yes)", [0, 1])

# -------- Prediction --------
if st.button("Predict"):
    input_data = {
        "season": season,
        "mnth": mnth,
        "weekday": weekday,
        "weathersit": weathersit,
        "temp": temp,
        "hum": hum,
        "windspeed": windspeed,
        "yr": yr,
        "holiday": holiday,
        "workingday": workingday
    }

    with st.spinner("Predicting..."):
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()["prediction"]
            st.subheader("📈 Prediction Result")
            st.success(f"🚴 Estimated Bike Demand: {int(result)} bikes/day")
        else:
            st.error("❌ API Error")
            st.write("Status Code:", response.status_code)
            st.write("Response:", response.text)

    