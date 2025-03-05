import pandas as pd
import logging
from src.datasets import Dataset

class Auto_EDA:
    def __init__(self, dataset: Dataset):
        # not df.copy() because this way df can be changes outside of this class
        self.dataset = dataset
        self.df = dataset.dataframe
        self.numerical_columns = self.df.describe().columns.tolist()
        self.categorical_columns = self.df.select_dtypes(exclude="number").columns.tolist()

    def numerical_columns(self) -> list:
        return self.numerical_columns

    def categorical_columns(self) -> list:
        return self.categorical_columns

    def unique_values(self, columns: list = None) -> dict:
        result = dict()
        if columns:
            # for a subset
            for col in columns:
                result[col] = self.df[col].nunique()
        else:
            # for entire dataframe
            for col in self.df.columns:
                result[col] = self.df[col].nunique()
                
        return result

    def print_eda_report(self):
        print(f"================= {self.dataset.label} =================")
        print(f"{self.dataset.label} has shape {self.dataset.dataframe.shape}")
        print()
        print(f"{self.dataset.label} has numerical data in columns: {self.numerical_columns}")
        numerical_dict = self.unique_values(columns=self.numerical_columns)
        for key, value in numerical_dict.items():
            print(f'- Column "{key}" has {value} unique values.')
        print()
        print(f"{self.dataset.label} has categorical data in columns: {self.categorical_columns}")
        categorical_dict = self.unique_values(columns=self.categorical_columns)
        for key, value in categorical_dict.items():
            print(f'- Column "{key}" has {value} unique values.')
        print()

