import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=";")

def filter_lines_by_id(data: pd.DataFrame, lines: list) -> pd.DataFrame:
    return data[data['route_id'].isin(lines)]