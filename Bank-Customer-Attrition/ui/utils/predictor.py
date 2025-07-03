# predictor.py
import joblib
from typing import Dict, Tuple, Optional
from utils.preprocessing import Preprocessor


class Predictor:
    def __init__(
        self, model_path: str, preprocessor: Preprocessor, feature_order: list
    ):
        self.model = joblib.load(model_path)
        self.preprocessor = preprocessor
        self.feature_order = feature_order

    def predict(self, input_dict: Dict) -> Tuple[int, Optional[float]]:
        # Performing fature engineering
        df = self.preprocessor.transform(input_dict)

        # Reorganizing the feature columns
        df = df[self.feature_order]

        # Making inference
        prediction = self.model.predict(df)[0]

        # probabillity
        proba = None
        if hasattr(self.model, "predict_proba"):
            proba = self.model.predict_proba(df)[0][1]

        return prediction, proba
