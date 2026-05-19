📈 Stock Market Dashboard (Streamlit Project)

🚀 Overview

The Stock Market Dashboard is an interactive web application built using Python and Streamlit that displays real-time stock market data and visualizations.

Users can enter any stock ticker symbol (such as AAPL, TSLA, or MSFT) and instantly view stock data along with a graphical representation of closing prices.

This project demonstrates practical use of:

- Streamlit dashboards
- API-based data fetching
- Data visualization
- Interactive web applications

---

🧠 Features

- Interactive web dashboard
- Fetches real-time stock data
- Displays stock data table
- Visualizes closing prices using graphs
- User-friendly interface

---

🛠️ Technologies Used

- Python
- Streamlit
- yfinance
- Pandas
- Matplotlib

---

⚙️ Installation & Setup

1. Clone the repository or download files

---

2. Install required libraries

pip install streamlit yfinance pandas matplotlib

---

3. Run the Streamlit application (on the terminal)

streamlit run app.py

---

💻 Complete Code ("app.py")

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("📈 Stock Market Dashboard")

# User input
stock = st.text_input("Enter Stock Symbol", "AAPL")

# Download stock data
data = yf.download(stock, period="1mo")

# Show stock data
st.subheader("Stock Data")
st.write(data)

# Create graph
fig, ax = plt.subplots()

ax.plot(data.index, data["Close"])

ax.set_title(f"{stock} Closing Prices")
ax.set_xlabel("Date")
ax.set_ylabel("Price")

# Display graph
st.pyplot(fig)

---

▶️ How It Works

1. User enters a stock ticker symbol
2. Application fetches stock data using "yfinance"
3. Data is displayed in a table format
4. A line graph visualizes stock closing prices
5. Streamlit converts the Python script into an interactive web app

---

📊 Example Output

Input

AAPL

Output

- Stock data table
- Interactive stock price graph
---

🎯 Skills Demonstrated

- Streamlit Web App Development
- API Integration
- Data Visualization
- Financial Data Analysis
- Interactive Dashboard Design

---

🔮 Future Improvements

- Add multiple stock comparison
- Add moving averages and indicators
- Add candlestick charts
- Add date range selection
- Deploy application online using Streamlit Cloud

---

👨‍💻 Author

Arsheen Shaikh

---
