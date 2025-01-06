import requests  

def get_weather(city_name, api_key):  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"  
    response = requests.get(base_url)  

    if response.status_code == 200:  
        data = response.json()  
        main = data['main']  
        weather = data['weather'][0]['description']  
        temperature = main['temp']  
        humidity = main['humidity']  # Get humidity  
        wind_speed = data['wind']['speed']  # Get wind speed  
        
        # Print weather details  
        print(f"Weather in {city_name}: {weather}")  
        print(f"Temperature: {temperature}°C")  
        print(f"Humidity: {humidity}%")  # Print humidity  
        print(f"Wind Speed: {wind_speed} m/s")  # Print wind speed  
    else:  
        print("City not found.")  

if __name__ == "__main__":  
    api_key = "73ec5798d1afd846bf8ff7e96f20fe11"  # Replace with your own OpenWeatherMap API key  
    city_name = input("Enter city name: ")  
    get_weather(city_name, api_key)