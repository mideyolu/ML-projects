# loader.py

import streamlit as st
from utils.features import cat_features, num_features, feature_order
from utils.predictor import Predictor
from utils.preprocessing import Preprocessor

# Initialize preprocessor and predictor
@st.cache_resource
def load_model_and_preprocessor():

    # Preprocessor
    preprocessor = Preprocessor(
        encoder_path="../models/churn_encoder.joblib",
        scaler_path="../models/churn_scaler.joblib",
        categorical_features=cat_features,
        numerical_features=num_features,
    )

    # Predictor
    predictor = Predictor(
        model_path="../models/churn_predictor.joblib",
        preprocessor=preprocessor,
        feature_order=feature_order,
    )

    return predictor

# loading predictor
predictor = load_model_and_preprocessor()
