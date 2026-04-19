import pickle
import pandas as pd

MODEL_PATH = "artifacts/bike_demand_model_v1.pkl"


# Step 1: Load trained model
def load_model():
    """
    Loads the trained machine learning pipeline from disk.

    Returns:
        Trained pipeline object
    """
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    return model


# Step 2: Load model once
model = load_model()


# Step 3: Prediction function
def predict(data):
    """
    This function takes input values (like season, temperature, etc.)
    and predicts the number of bikes required.
    """
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction[0]  

   