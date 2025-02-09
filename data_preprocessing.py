import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(df):
    # Select 'Close' price as target variable
    data = df[['Close']].values
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)
    return data_scaled, scaler

if __name__ == "__main__":
    import data_fetch
    df = data_fetch.fetch_stock_data("AAPL")
    data_scaled, scaler = preprocess_data(df)
    print(data_scaled[:5])
