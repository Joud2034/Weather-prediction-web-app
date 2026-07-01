from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load Model
model = joblib.load("rain_prediction_model_new.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    user_data = pd.DataFrame([{

        "MinTemp": float(request.form["MinTemp"]),
        "MaxTemp": float(request.form["MaxTemp"]),
        "Rainfall": float(request.form["Rainfall"]),
        "Humidity9am": float(request.form["Humidity9am"]),
        "Humidity3pm": float(request.form["Humidity3pm"]),
        "Pressure9am": float(request.form["Pressure9am"]),
        "Pressure3pm": float(request.form["Pressure3pm"]),

        "RainToday": 1 if request.form["RainToday"] == "Yes" else 0

    }])
    

    prediction = model.predict(user_data)[0]
    prob = model.predict_proba(user_data)[0]

    confidence = max(prob) * 100

    prediction = model.predict(user_data)[0]

    if prediction == "Yes":
        result = "🌧 Rain Expected Tomorrow"
        result_class = "yes"
    else:
        result = "☀ No Rain Expected Tomorrow"
        result_class = "no"
    
    

    return render_template(
    "index.html",
    prediction=result,
    confidence=f"{confidence:.1f}%",
    result_class=result_class
)


if __name__ == "__main__":
    app.run(debug=True)

