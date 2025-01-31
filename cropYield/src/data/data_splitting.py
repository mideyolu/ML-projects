# data/data_splitting.py

import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(
        input_data_path, output_train_path, output_test_path, target_column, test_size, seed
):
    """
        Split the dataset into training and testing sets and save them to specified paths.

        Args:
        - input_data_path (str): Path to the input dataset (CSV file).
        - output_train_path (str): Path to save the training dataset.
        - output_test_path (str): Path to save the testing dataset.
        - target_column (str): Name of the target column (dependent variable).
        - test_size (float): Proportion of the data to be used as the test set.
        - seed (int): Random seed for reproducibility.

        Returns:
        - None
    """

    # Load the dataset

    df = pd.read_csv(input_data_path)

    # Ensure the target column exists
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not in input dataframe")

    # Separate features and target
    X = df.drop(columns=[target_column])
    y= df[target_column]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed
    )

    # Combine features and target for saving

    train_data = pd.concat(
        [
            X_train, y_train
        ], axis=1
    )
    test_data = pd.concat(
        [
            X_test, y_test
        ], axis=1
    )


    train_data.to_csv(
        output_train_path, index=False
    )

    test_data.to_csv(
        output_test_path, index=False
    )

    print(f"Training data saved to {output_train_path}")
    print(f"Testing data saved to {output_test_path}")
