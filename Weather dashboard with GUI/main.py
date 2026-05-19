import tkinter as tk
import requests

API_KEY = "YOUR_REAL_API_KEY"

def get_weather():

    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    # Debug print
    print(response.json())

    data = response.json()

    if response.status_code == 200:

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=f"Temperature: {temp}°C\nWeather: {weather}"
        )

    else:
        result_label.config(text="City not found")


# GUI
root = tk.Tk()
root.title("Weather Dashboard")

city_entry = tk.Entry(root)
city_entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()