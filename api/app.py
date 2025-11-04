from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/linear-regression/predict/<volume>")
def predict(volume: float):
    with open("static/linear_regression.json") as file:
        model = json.load()

    slope, intercept = model["coefficients"]
    
    prediction = {
        "CO2 Emission": slope * volume + intercept
    }

    return jsonify(prediction)

if "__main__" == __name__:
    app.run(debug=True)
