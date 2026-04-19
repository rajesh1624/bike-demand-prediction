from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def get_preprocessor():

    categorical_features = ['season','mnth','weekday','weathersit']
    numerical_features = ['temp','hum','windspeed']
    binary_features = ['yr','holiday','workingday']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features),
            ('num', StandardScaler(), numerical_features),
            ('bin', 'passthrough', binary_features)
        ]
    )

    return preprocessor