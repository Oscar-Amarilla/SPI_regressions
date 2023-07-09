import pandas as pd

def to_time_series(dataframe):
    time_series = []
    for index,row in dataframe.iterrows():
        time_series += list(dataframe.iloc[index].values)
    return time_series
