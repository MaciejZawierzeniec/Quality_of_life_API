import pandas as pd


def read_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
