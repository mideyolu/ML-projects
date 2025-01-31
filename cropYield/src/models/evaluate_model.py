# src/models/evaluate_model.py

import pandas as pd
import joblib
from sklearn.metrics import root_mean_squared_error


def evaluate_model(
        test_data_path, target_column, model_path
):
    """
     Evaluate the trained regression model on the test dataset

     Args:
       - test_data_path (str): Path to the test dataset (CSV file)
       - target_column (str): Name of the target column (dependent variable)
       - model_path (str): Path to the saved model

     Returns:
       - rmse (float): Root Mean Squared Error on th test data
    """

    # Load the test dataset
    df = pd.read_csv(test_data_path)

    # Ensure the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not in input dataframe")


    # Separate the features and target
    X = df.drop(columns=[target_column])
    y= df[target_column]

    # Load the trained model
    model = joblib.load(
        model_path
    )

    # Predict on the data
    y_pred = model.predict(X)

    # Calculate the RMSE
    rmse = root_mean_squared_error(
        y_true=y,
        y_pred=y_pred
    )

    output = f"RMSE: {rmse:.3f}"

    print(output)

    return output


# # Example usage
# if __name__ == "__main__":
#     evaluate_model(
#         test_data_path='data/test/test_data.csv',
#         target_column='crop_yield',
#         model_path='models/crop_yield_prediction_model.pkl'
#     )
