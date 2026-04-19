import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from src.data_cleaning import load_data, clean_data
from src.transformation import get_preprocessor
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np
DATA_PATH = "data/raw/day.csv"
MODEL_PATH = "artifacts/bike_demand_model_v1.pkl"

def train_model():
    """
    Train and save the bike demand prediction model.

    This function performs the following steps:
    - Loads raw data from the data folder
    - Cleans the dataset and applies preprocessing using a pipeline
    - Splits data into training and testing sets
    - Applies feature transformations using a preprocessing pipeline
    - Trains a Linear Regression model
    - Saves the trained pipeline as a .pkl file in the artifacts folder

    Returns:
        None
    """

    # Step 1: Load data
    df = load_data(DATA_PATH)

    # Step 2: Clean data
    df = clean_data(df)

    # Step 3: Separate features and target
    X = df.drop('cnt', axis=1)
    y = df['cnt']

    # Step 4: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Step 5: Get preprocessor
    preprocessor = get_preprocessor()

    # Step 6: Create pipeline
    pipeline = Pipeline([
        ('preprocessing', preprocessor),
        ('model', LinearRegression())
    ])

    # Step 7: Train model
    pipeline.fit(X_train, y_train)

    # Step 8: Evaluate model
    y_pred = pipeline.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print("Model: Linear Regression (Baseline)")
    print(f"R2 Score: {r2:.4f}")
    print(f"RMSE: {rmse:.4f}")

    # Step 9: Save model
    print("Saving model to:", MODEL_PATH)
    
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(pipeline, f)

    print("Model trained and saved successfully!")


if __name__ == "__main__":
    train_model()