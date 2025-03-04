import pandas as pd

def numerical_data_columns(df: pd.DataFrame) -> list:
    """"
    This is a test method, it does nothing valuable yet.
    """
    
    return df.describe().columns.tolist()