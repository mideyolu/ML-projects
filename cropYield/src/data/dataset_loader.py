# src/data/dataset_loader.py

import pandas as pd


def load_data(file_path):
    """
    Load the dataset from a CSV file into a pandas DataFrame.

    Args:
    - file_path (str): The file path to the dataset.

    Returns:
    - pd.DataFrame: The loaded dataset.
    """

    #loading the data
    df = pd.read_csv(file_path)


    return df

