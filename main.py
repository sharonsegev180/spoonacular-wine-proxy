from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Spoonacular Wine Proxy is running!'

@app.route('/wine-pairing')
def wine_pairing():
    food = request.args.get('food')
    if not food:
        return jsonify({"error": "Missing 'food' query parameter"}), 400

    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        return jsonify({"error": "RAPIDAPI_KEY not set in environment"}), 500

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/pairing"
    querystring = {"food": food}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        print("API Response:", data)  # לוג מעקב ב-Render

        return jsonify(data)

    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return jsonify({"error": "HTTP error occurred", "details": str(errh)}), 500
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", errc)
        return jsonify({"error": "Connection error occurred", "details": str(errc)}), 500
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return jsonify({"error": "Timeout error occurred", "details": str(errt)}), 500
    except requests.exceptions.RequestException as err:
        print("General Error:", err)
        return jsonify({"error": "An error occurred", "details": str(err)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
