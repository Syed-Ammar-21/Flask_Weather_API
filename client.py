import requests

def get_weather(city):
    url = 'http://127.0.0.1:5000/weather'
    params = {'city': city}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
    else:
        print(f"Error: {response.json().get('error', 'Unknown error occurred')}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)

