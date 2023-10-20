import requests
def my_func(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        print(f"weather in {city}: {temperature}°C, {weather_description} ")
    else:
        print("unable to fetch weather data.please check the city name or API KEY")

if __name__ == "__main__":
    api_key ="c8dc434a2ae840a3b046a3eb5e83a4c7"
    while True:
        city = input("Enter the city name (or type 'exit' to quit):")
        if city.lower() == 'exit':
            break
        my_func(api_key, city)