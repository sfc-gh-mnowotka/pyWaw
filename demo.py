from datetime import date
from dateutil.relativedelta import relativedelta

import streamlit as st
import yfinance as yf

st.title("Demo App!")
st.header(":snake: pyWaw demo")
st.write("---")

POPULAR_STOCKS = ["TSLA", "AAPL", "AMZN", "MSFT", "META", "GOOGL", "SNOW",
                  "NVDA", "NFLX", "PLTR", "INTC", "COIN", "ADBE", "ZM"]

today = date.today()
two_years_ago = today - relativedelta(years=2)

if "tickers" not in st.session_state:
    st.session_state["tickers"] = ["SNOW", "COIN"]

if "dates" not in st.session_state:
    st.session_state["dates"] = [today - relativedelta(years=2), today]

if "interval" not in st.session_state:
    st.session_state["interval"] = "1d"    

tickers = st.multiselect("Choose ticker", POPULAR_STOCKS,
                         key="tickers")
start, end = st.slider("Date range:", key="dates")
interval = st.select_slider("Interval", ["1d", "5d", "1wk","1mo", "3mo"],
                            key="interval")

data = yf.Tickers(" ".join(tickers))
df = data.history(start=start, end=end, interval=interval)

with st.expander("Raw data"):
    st.write(df)

st.line_chart(df.Close)
st.line_chart(df.Volume)
