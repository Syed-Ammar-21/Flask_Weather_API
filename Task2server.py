from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
API_KEY = '3ff57dff9da89d2043b3a2a28ebc3f28'  # Replace with your real API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 404:
        return jsonify({'error': 'Invalid city name. Please enter a valid city.'}), 404
    
    # If any other error occurs
    if response.status_code != 200:
        return jsonify({'error': 'Could not retrieve weather data'}), response.status_code
    weather_data = response.json()
    result = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'humidity': weather_data['main']['humidity'],
        'wind_speed': weather_data['wind']['speed'],
        'pressure': weather_data['main']['pressure']
    }
    return jsonify(result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
