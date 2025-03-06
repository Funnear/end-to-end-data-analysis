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
        self.init_rows = self.count_rows()
        self.init_cols = self.count_cols()

        # DYNAMIC context: need to be refreshed before using
        self.numerical_columns = self.get_numerical_columns()
        self.categorical_columns = self.get_categorical_columns()
        

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
    
    def count_cols(self):
        return self.dataset.dataframe.shape[1]
    
    def descriptive_numerical(self):
        # df[num_cols].describe().T
        # analysis_dict_row['mode'] = column.mode().tolist()
        # analysis_dict_row['standard deviation'] = column.std()
        # analysis_dict_row['dispersion range'] = column.max() - column.min()
        # column_names_list = ['mean', 'median', 'mode', 'standard deviation', 'dispersion range']
        # stats_for_numerical_columns = result_df[result_df['is_numerical'] == True][column_names_list]
        pass

    def descriptive_categorical(self):
        # analysis_dict_row['frequency counts'] = column.value_counts().to_dict()
        # categorical_columns = result_df[result_df['is_categorical'] == True]['frequency counts']

        # for column, freq_dict in categorical_columns.items():
        #     print(f"\nFrequency counts for {column}:")
        #     freq_df = pd.DataFrame(list(freq_dict.items()), columns=['Category', 'Count'])
        #     print(freq_df)
        pass

    def print_eda_report(self):
        # TODO: save the report as a text file automatically.
        self.numerical_columns = self.get_numerical_columns()
        self.categorical_columns = self.get_categorical_columns()

        print(f"================= {self.dataset.label} =================")
        print(f"{self.dataset.label} has shape {self.df.shape}")
        print()

        print(f"{self.dataset.label} has numerical data in columns: {self.numerical_columns}")
        numerical_dict = self.unique_values(columns=self.numerical_columns)
        
        # sorting dictionary by values descending
        # lambda function for bonus points!
        numerical_dict = dict(sorted(numerical_dict.items(), key=lambda item: item[1], reverse=True))

        for key, value in numerical_dict.items():
            print(f'- Column "{key}" has {value} unique values.')
            if value <= 20:
                print(f"   -- Unique values are:\n {self.df[key].unique()}")

        print()
        
        # print("Descriptive statistics for numerical data:")
        # self.descriptive_numerical()

        # TODO: code duplication
        print(f"{self.dataset.label} has categorical data in columns: {self.categorical_columns}")
        categorical_dict = self.unique_values(columns=self.categorical_columns)

        for key, value in categorical_dict.items():
            print(f'- Column "{key}" has {value} unique values.')
            if value <= 20:
                print(f"  -- Unique values are:\n {self.df[key].unique()}")

        print()

        # print("Descriptive statistics for categorical data:")
        # self.descriptive_categorical()
    # END OF PRINT EDA
        
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
        df_nulls["na_percent"] = (df_nulls["is_na"] / self.count_rows() * 100)
        # MAP for bonus points
        df_nulls["na_percent_pretty"] = df_nulls["na_percent"].map("{:.2f}%".format)
        df_nulls.sort_values(by=["na_percent", "is_na"], ascending=[False, False], inplace=True)
        return df_nulls
