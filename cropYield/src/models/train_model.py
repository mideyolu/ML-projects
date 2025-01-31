# src/models/train_model.py

import pandas as pd
from lightgbm import LGBMRegressor
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.model_save import save_model



def train_model(train_data_path, target_column, seed, model_output_path):
    """
    Train a regression model on the provided dataset.

    Args:
        - train_data_path (str): Path to the cleaned and processed dataset (CSV file).
        - target_column (str): The name of the target column (dependent variable).
        - seed (int): Random seed for model reproducibility.
        - model_output_path (str): Path to save the trained model.

    Returns:
        - None
    """

    # Load the dataset
    df = pd.read_csv(train_data_path)

    # Ensure the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not in input dataframe.")

    # Separate the features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Initialize the LightGBM model
    model = LGBMRegressor(
        objective='regression',
        random_state=seed
    )

    # Train the model
    model.fit(X=X, y=y)

    # Save the trained model using the utility function
    save_model(model, model_output_path)
