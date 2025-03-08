from flask import Flask, request, jsonify
import requests
app = Flask(__name__)
API_KEY = '3ff57dff9da89d2043b3a2a28ebc3f28'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
@app.route('/weather', methods=['GET'])
def get_weather():
    cities = request.args.get('cities')  
    if not cities:
        return jsonify({'error': 'Cities parameter is required'}), 400  
    city_list = [city.strip() for city in cities.split(",")]  
    weather_results = []
    for city in city_list:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 404:
            weather_results.append({'city': city, 'error': 'Invalid city name. Please enter a valid city.'})
        elif response.status_code != 200:
            weather_results.append({'city': city, 'error': 'Could not retrieve weather data'})
        else:
            weather_data = response.json()
            weather_results.append({
                'city': weather_data['name'],
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'wind_speed': weather_data['wind']['speed'],
                'pressure': weather_data['main']['pressure']
            })
    return jsonify(weather_results)  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
