from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import predict

app = FastAPI()

# Request schema
class InputData(BaseModel):
    season: int
    mnth: int
    weekday: int
    weathersit: int
    temp: float
    hum: float
    windspeed: float
    yr: int
    holiday: int
    workingday: int

@app.get("/")
def home():
    return {"message": "Bike Demand Prediction API is running"}

@app.post("/predict")
def predict_demand(data: InputData):
    try:
        input_dict = data.model_dump()
        result = predict(input_dict)
        return {"prediction": max(0, int(result))}
    except Exception as e:
        return {"error": str(e)}