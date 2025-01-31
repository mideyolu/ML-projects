# src/data/dataset_cleaning.py

import pandas as pd

def clean_data(df):
    """
        Clean the input dataframe by handling missing values and outliers.

        Args:
        - df (pd.DataFrame): The raw data.

        Returns:
        - pd.DataFrame: The cleaned data.
    """

    # Handle missing values by removing rows with any missing values
    df = df.dropna()

    #removing outliers using IQR
    for column in ['rainfall_mm','soil_quality_index','farm_size_hectares','sunlight_hours','fertilizer_kg','crop_yield']:

        """
            Loop through the columns/features provided find the lower and upper bound then handle outliers.
        """

        # First quartile
        Q1 = df[column].quantile(0.25)
        # Second quartile
        Q3 = df[column].quantile(0.75)

        # IQR range
        IQR = Q3 - Q1

        # Lower bound
        lower_bound= Q1 - 1.5 * IQR
        # Upper bound
        upper_bound = Q3 + 1.5 * IQR

        # Remove the affected rows outside the IQR bounds
        df = df[(df[column] >=lower_bound) & (df[column]<=upper_bound)]


    # Ensure proper data formats for numerical columns (preferably floats rather than int)
    df['rainfall_mm'] = df['rainfall_mm'].astype(float)
    df['soil_quality_index'] = df['soil_quality_index'].astype(float)
    df['farm_size_hectares'] = df['farm_size_hectares'].astype(float)
    df['sunlight_hours'] = df['sunlight_hours'].astype(float)
    df['crop_yield'] = df['crop_yield'].astype(float)


    return df
