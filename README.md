# Weather-prediction-web-app

# 🌦 Weather Prediction Web App

A machine learning web application that predicts whether it will rain tomorrow based on weather observations.

## 📌 Project Overview

This project uses a Random Forest Classifier trained on weather data to predict rainfall for the next day. The trained model is deployed through a Flask web application with a simple and user-friendly interface.

## 🚀 Features

- Predicts whether it will rain tomorrow.
- Simple web interface built with Flask.
- Real-time predictions.
- Displays the prediction confidence.
- Trained using selected weather features for a lightweight and efficient model.

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- HTML
- CSS
- Joblib

## 📊 Input Features

The model uses the following weather observations:

- Minimum Temperature
- Maximum Temperature
- Rainfall
- Humidity (9 AM)
- Humidity (3 PM)
- Pressure (9 AM)
- Pressure (3 PM)
- Rain Today

## 📈 Model

- Algorithm: Random Forest Classifier
- Accuracy: ~84%
- ROC-AUC: ~0.84

## ▶️ Run the Project

Clone the repository:

```bash
git clone https://github.com/Joud2034/weather-prediction-web-app.git
```

Install the required packages:

```bash
pip install flask
```

Run the application:

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

## 👩‍💻 Author

Developed by **Joud**
