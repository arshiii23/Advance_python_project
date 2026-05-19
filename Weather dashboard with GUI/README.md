🌦️ Weather Dashboard GUI (Python API Project)

🚀 Overview

The Weather Dashboard GUI is a Python-based desktop application that fetches and displays real-time weather information using the OpenWeatherMap API.

The project provides a simple graphical user interface (GUI) where users can enter a city name and instantly view current temperature and weather conditions.

This project demonstrates practical use of:

- GUI development
- API integration
- Real-time data fetching
- Error handling

---

🧠 Features

- Simple graphical interface using Tkinter
- Fetches live weather data
- Displays:
  - Temperature
  - Weather condition
- User-friendly design
- Handles invalid city names and API errors

---

🛠️ Technologies Used

- Python
- Tkinter
- Requests Library
- OpenWeatherMap API

⚙️ Installation & Setup

1. Clone the repository or download the files

2. Install required library:

pip install requests

3. Get a free API key from:
   "OpenWeatherMap API" (https://openweathermap.org/api?utm_source=chatgpt.com)

4. Replace your API key in "main.py":

API_KEY = "YOUR_API_KEY"

5. Run the project:

python main.py

# GUI Window
root = tk.Tk()
root.title("Weather Dashboard")

city_entry = tk.Entry(root)
city_entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

---

▶️ How It Works

1. User enters a city name
2. Application sends request to OpenWeatherMap API
3. API returns weather data in JSON format
4. Program extracts:
   - Temperature
   - Weather description
5. Results are displayed in the GUI window

---

🎯 Skills Demonstrated

- GUI Development
- API Integration
- JSON Data Handling
- Error Handling
- Real-time Data Fetching
- Python Application Development

---

🔮 Future Improvements

- Add weather icons
- Add humidity and wind speed
- Display 5-day weather forecast
- Improve GUI styling
- Convert into Streamlit web app

---

👨‍💻 Author

Arsheen Shaikh

---
