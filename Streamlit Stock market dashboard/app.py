import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt


# TITLE

st.title("📈 Stock Market Dashboard")

# -------------------------
# USER INPUT
# -------------------------

stock = st.text_input("Enter Stock Symbol", "AAPL")

# -------------------------
# DOWNLOAD STOCK DATA
# -------------------------

data = yf.download(stock, period="1mo")

# -------------------------
# SHOW DATA
# -------------------------

st.subheader("Stock Data")

st.write(data)

# -------------------------
# CREATE GRAPH
# -------------------------

fig, ax = plt.subplots()

ax.plot(data.index, data["Close"])

ax.set_title(f"{stock} Closing Prices")

ax.set_xlabel("Date")
ax.set_ylabel("Price")

# -------------------------
# DISPLAY GRAPH
# -------------------------

st.pyplot(fig)
