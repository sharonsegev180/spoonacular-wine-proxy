from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY') or 'הכניסי_כאן_ידנית_אם_רוצה'
RAPIDAPI_HOST = "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"

@app.route('/wine-pairing', methods=['GET'])
def wine_pairing():
    food = request.args.get('food')
    url = f"https://{RAPIDAPI_HOST}/food/wine/pairing"
    querystring = {"food": food}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
