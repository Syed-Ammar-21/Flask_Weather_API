import requests

def get_weather(cities):
    url = 'http://127.0.0.1:5000/weather'  
    params = {'cities': cities}  
    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        for city_data in weather_data:
            if 'error' in city_data:
                print(f"\nCity: {city_data['city']} - Error: {city_data['error']}")
            else:
                print(f"\nCity: {city_data['city']}")
                print(f"Temperature: {city_data['temperature']}°C")
                print(f"Description: {city_data['description']}")
                print(f"Humidity: {city_data['humidity']}%")
                print(f"Wind Speed: {city_data['wind_speed']} m/s")
                print(f"Pressure: {city_data['pressure']} hPa")
    else:
        print("Error: Could not retrieve weather data.")

if __name__ == "__main__":
    city_names = input("Enter city names (comma-separated): ")
    get_weather(city_names)
