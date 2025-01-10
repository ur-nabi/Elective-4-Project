import requests

def get_weather(city):
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = '20330c6ef29e36c05f57067e42e6bdec'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Request parameters
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Fetch temperature in Celsius
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the response is successful
        if data['cod'] == 200:
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            print(f"Weather in {city}: {weather.capitalize()}, {temp}°C")
        else:
            print(f"City '{city}' not found. Please check the city name.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

# Example usage
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
