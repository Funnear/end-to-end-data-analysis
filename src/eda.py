import pandas as pd
import numpy as np
import logging
from src.datasets import Dataset

class Auto_EDA:
    def __init__(self, dataset: Dataset):
        # not df.copy() because this way df can be changes outside of this class
        # STATIC context
        self.dataset = dataset
        self.df = dataset.dataframe

        # DYNAMIC context: need to be refreshed before using
        self.numerical_columns = self.get_numerical_columns()
        self.categorical_columns = self.get_categorical_columns()
        self.n_rows = self.count_rows()

    def get_numerical_columns(self) -> list:
        return self.df.describe().columns.tolist()

    def get_categorical_columns(self) -> list:
        return self.df.select_dtypes(exclude="number").columns.tolist()

    def unique_values(self, columns: list = None) -> dict:
        result = dict()
        if not columns:
            # for entire dataset
            columns = self.df.columns
        
        # by default - for a subset specified by a column list
        for col in columns:
            result[col] = self.df[col].nunique()
                
        return result
    
    def count_rows(self):
        return self.dataset.dataframe.shape[0]

    def print_eda_report(self):
        print(f"================= {self.dataset.label} =================")
        print(f"{self.dataset.label} has shape {self.df.shape}")
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
        
    def auto_cleanup(self):
        # find and remove empty spaces
        has_empty_spaces = (self.df.eq(" ").sum().sum() > 0)

        if has_empty_spaces:
            self.df.replace(" ", np.nan, inplace=True)
            logging.info(f"{self.dataset.label} had empty spaces in some columns. They are replaced with NaN.")
        else:
            logging.info(f"{self.dataset.label} has no empty spaces.")

        # find and remove dupolicates
        has_duplicates = False if int(self.df.duplicated().sum()) == 0 else True
        
        if has_duplicates:
            self.df.drop_duplicates(inplace=True)
            self.df.reset_index(drop=True, inplace=True)
            logging.info(f"{self.dataset.label} had duplicates. They had been dropped and index was reset.")
        else:
            logging.info(f"{self.dataset.label} has no duplicates.")

    def count_nulls(self) -> pd.DataFrame:
        df_nulls = pd.concat([self.df.isna().sum(), self.df.notna().sum()], ignore_index=True, axis=1)
        df_nulls.columns=['is_na', 'not_na']
        df_nulls["na_percent"] = (df_nulls["is_na"] / self.df.shape[0] * 100).map("{:.2f}%".format)
        df_nulls.sort_values(by=["na_percent", "is_na"], ascending=[False, False], inplace=True)
        return df_nulls