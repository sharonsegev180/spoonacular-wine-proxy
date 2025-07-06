from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY") or "הכניסי כאן את המפתח שלך אם תרצי קידוד קשיח"

@app.route("/wine-pairing")
def wine_pairing():
    food = request.args.get("food")
    if not food:
        return jsonify({"error": "Missing 'food' parameter"}), 400

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/pairing"
    querystring = {"food": food}

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return jsonify(response.json())

@app.route("/")
def home():
    return "Spoonacular Wine Proxy is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

