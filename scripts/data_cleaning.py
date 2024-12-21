# Import basic Libraries 
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

class TelecomDataCleaner:
    """
    A class for cleaning and preprocessing telecom datasets.
    """
    def __init__(self, essential_columns=None, unnecessary_columns=None):
        self.essential_columns = essential_columns if essential_columns else ['Bearer Id']
        self.unnecessary_columns = unnecessary_columns if unnecessary_columns else ['Unnamed: 0', 'id']
    
    def clean_data(self, df):
        """
        Cleans the telecom dataset by handling missing values, outliers, and ensuring proper data types.
        """
        # 1. Drop columns with more than 50% missing data
        df = df.loc[:, df.isnull().mean() < 0.5]
        
        # 2. Drop rows with null values in essential columns
        df.dropna(subset=self.essential_columns, inplace=True)
        
        # 3. Convert object columns to category and fill missing values with mode
        object_cols = df.select_dtypes(include=['object']).columns
        for col in object_cols:
            df[col] = df[col].astype('category')
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        # 4. Handle Missing Values for numerical columns
        numerical_cols = df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            df[col].fillna(df[col].mean(), inplace=True)
        
        # 5. Handle Outliers using Z-score
        for col in numerical_cols:
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            df = df[z_scores < 3]  # Remove rows where Z-score > 3 (outliers)
        
        # 6. Standardize Date Columns
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # 7. Remove Duplicates
        df.drop_duplicates(inplace=True)
        
        # 8. Remove Unnecessary Columns
        df.drop(columns=[col for col in self.unnecessary_columns if col in df.columns], inplace=True)
        
        print("Data Cleaning Complete!")
        return df
    
    def standardize_datetime_columns(self, df, date_columns):
        """
        Converts specified date-time columns into standard date format.
        """
        for col in date_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.date
        print("Date-Time Columns Standardized!")
        return df



