# preprocessing.py
import joblib
import pandas as pd
from typing import Dict, List


class Preprocessor:
    def __init__(
        self,
        encoder_path: str,
        scaler_path: str,
        categorical_features: List[str],
        numerical_features: List[str],
    ):
        self.encoders = joblib.load(encoder_path)
        self.scalers = joblib.load(scaler_path)
        self.categorical_features = categorical_features
        self.numerical_features = numerical_features

    def transform(self, input_dict: Dict) -> pd.DataFrame:
        # creating the dataframe
        df = pd.DataFrame([input_dict])

        # Encode categorical
        for col in self.categorical_features:
            le = self.encoders[col]
            df[col] = le.transform([df.at[0, col]])[0]

        # Scale numerical
        for col in self.numerical_features:
            scaler = self.scalers[col]
            df[col] = scaler.transform(df[[col]]).flatten()

        return df
