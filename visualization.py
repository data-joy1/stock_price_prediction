import matplotlib.pyplot as plt

def plot_predictions(actual, predicted):
    plt.figure(figsize=(10,5))
    plt.plot(actual, label="Actual Prices")
    plt.plot(predicted, label="Predicted Prices")
    plt.legend()
    plt.title("Stock Price Prediction")
    plt.show()

if __name__ == "__main__":
    import lstm_model
    import data_fetch, data_preprocessing
    import numpy as np

    df = data_fetch.fetch_stock_data("AAPL")
    data_scaled, scaler = data_preprocessing.preprocess_data(df)

    X, y = lstm_model.create_sequences(data_scaled)
    model = tf.keras.models.load_model("lstm_stock_model.h5")

    predictions = model.predict(X)
    predictions = scaler.inverse_transform(predictions)
    plot_predictions(df['Close'][-len(predictions):], predictions)
