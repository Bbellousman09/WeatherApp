import requests  
import tkinter as tk  
from tkinter import messagebox  

def get_weather(city_name, api_key):  
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"  
    response = requests.get(base_url)  

    if response.status_code == 200:  
        data = response.json()  
        main = data['main']  
        weather = data['weather'][0]['description']  
        temperature = main['temp']  
        humidity = main['humidity']  
        wind_speed = data['wind']['speed']  
        
        # Update result in the GUI  
        result_text = (f"Weather in {city_name}:\n"  
                       f"Description: {weather}\n"  
                       f"Temperature: {temperature}°C\n"  
                       f"Humidity: {humidity}%\n"  
                       f"Wind Speed: {wind_speed} m/s")  
        result_label.config(text=result_text)  
    else:  
        messagebox.showerror("Error", "City not found.")  

def fetch_weather():  
    city_name = city_entry.get().strip()  
    if city_name:  
        get_weather(city_name, api_key)  
    else:  
        messagebox.showwarning("Input Error", "Please enter a city name.")  

if __name__ == "__main__":  
    api_key = "73ec5798d1afd846bf8ff7e96f20fe11"  # Replace with your OpenWeatherMap API key  

    # Create the main window  
    root = tk.Tk()  
    root.title("Weather App")  

    # Input field for city name  
    city_label = tk.Label(root, text="Enter City Name:")  
    city_label.pack(pady=10)  

    city_entry = tk.Entry(root)  
    city_entry.pack(pady=5)  

    # Fetch weather button  
    fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)  
    fetch_button.pack(pady=10)  

    # Label to display results  
    result_label = tk.Label(root, text="", justify=tk.LEFT)  
    result_label.pack(pady=10)  

    # Run the GUI loop  
    root.mainloop()