# src/utils/model_save.py

import os
import joblib

def save_model(model, model_output_path):
    """
    Save the trained model to the specified path.

    Args:
        model (object): The trained model to be saved.
        model_output_path (str): Path to save the trained model.

    Returns:
        None
    """
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)
    print(f"Model saved to: {model_output_path}")

def load_model(model_path):
    """
    Load a trained model from the specified path.

    Args:
        model_path (str): Path to the saved model.

    Returns:
        object: The loaded model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    model = joblib.load(model_path)
    print(f"Model loaded from: {model_path}")
    return model
