📈 Stock Price Prediction using LSTM
📌 Project Overview
This project predicts future stock prices using Long Short-Term Memory (LSTM) networks, a type of Recurrent Neural Network (RNN) specialized for time-series forecasting. We use Yahoo Finance API to fetch historical stock data and train an LSTM model to make predictions.

📂 Project Structure
📂 stock_price_prediction/
├── 📄 data_fetch.py         # Fetch stock data from Yahoo Finance
├── 📄 data_preprocessing.py # Normalize & preprocess data
├── 📄 lstm_model.py         # Train the LSTM model
├── 📄 visualization.py      # Plot actual vs predicted prices
├── 📄 main.py               # Run the entire pipeline
├── 📄 requirements.txt      # Dependencies list
├── 📄 README.md             # Project documentation

🛠️ Technologies Used
Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TensorFlow/Keras, Yahoo Finance API
Machine Learning Model: LSTM (Long Short-Term Memory)

📊 Dataset Used
Source: Yahoo Finance API
Features Used:
✅ Date – Timestamp of stock price
✅ Open – Opening price
✅ High – Highest price of the day
✅ Low – Lowest price of the day
✅ Close – Closing price (Target Variable ✅)
✅ Volume – Number of shares traded

📌 Steps to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/data-joy1/stock_price_prediction.git
cd stock_price_prediction

2️⃣ Create Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Run the Project
python main.py

📊 Key Features & Results
✅ Fetch real-time stock data using Yahoo Finance API.
✅ Train an LSTM model for time-series forecasting.
✅ Use MinMaxScaler to normalize stock prices.
✅ Visualize actual vs predicted stock prices using Matplotlib.

📈 Visualization Example
