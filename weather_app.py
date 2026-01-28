import tkinter as tk
from tkinter import messagebox
import requests
window = tk.Tk()
window.title("Weather App")
window.geometry("350x300")
def get_weather():
    city = city_entry.get()
    
    if city=="":
        messagebox.showwarning("Warning", "Please enter the a city name")
        return
    api_key = "bada6824596db1bcea6623f3647825d2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("error", "City not found")
            return
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        result_label.config(
            text = f"Temperature: {temperature}°C\n"
                   f"Humidity: {humidity}%\n"
                   f"Weather: {description.capitalize()}"
            )
    except:
        messagebox.showerror("Error", "Could not fetch weather data")
###ui elements
tk.Label(window, width = 25, font=("Arial", 12))
city_entry = tk.Entry(window, width = 25, font=("Arial", 12))
city_entry.pack(pady=5)
tk.Button(window, text="Get Weather", width = 15, command = get_weather).pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady = 10)

window.mainloop
    