from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.realpath(__file__)), 'index.html')

@app.route('/get_weather', methods=['GET'])
def get_weather():

    latitude = 51.14
    longitude = 17.11

    index_day_in = 24
    index_day_out = 31

    api_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
        f"&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    try:
        response = requests.get(api_url)
        data = response.json()

        weather_data_day = {
            "temperature": data['hourly']['temperature_2m'][index_day_in],
            "relative_humidity": data['hourly']['relative_humidity_2m'][index_day_in],
            "wind_speed": data['hourly']['wind_speed_10m'][index_day_in],
        }

        weather_data_night = {
            "temperature": data['hourly']['temperature_2m'][index_day_out],
            "relative_humidity": data['hourly']['relative_humidity_2m'][index_day_out],
            "wind_speed": data['hourly']['wind_speed_10m'][index_day_out],
        }

        return jsonify({"day": weather_data_day, "night": weather_data_night})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

@app.route('/get_alternate_weather', methods=['GET'])
def get_alternate_weather():

    latitude = 51.14
    longitude = 17.11

    index_day_in = 15
    index_day_out = 25

    api_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m"
        f"&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )

    try:
        response = requests.get(api_url)
        data = response.json()

        weather_data_day = {
            "temperature": data['hourly']['temperature_2m'][index_day_in],
            "relative_humidity": data['hourly']['relative_humidity_2m'][index_day_in],
            "wind_speed": data['hourly']['wind_speed_10m'][index_day_in],
        }

        weather_data_night = {
            "temperature": data['hourly']['temperature_2m'][index_day_out],
            "relative_humidity": data['hourly']['relative_humidity_2m'][index_day_out],
            "wind_speed": data['hourly']['wind_speed_10m'][index_day_out],
        }

        return jsonify({"day": weather_data_day, "night": weather_data_night})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)