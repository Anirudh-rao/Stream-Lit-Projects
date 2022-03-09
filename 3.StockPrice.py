import yfinance as yf
import streamlit as st
import pandas as pd



st.write("""
# Simple Stock Price App
Shown are the stock closing and Volume of Google
""")

#Define Ticker symbol
tickersymbol = 'GOOGL'

#Get Ticker Data
tickerdata =  yf.Ticker(tickersymbol)

tickerDf  =  tickerdata.history(period='1d',start='2010-5-31',end='2020-5-31')


#open High Low and Close Volume Divedends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


"""Run the Following Command in the Terminal to Run the Application
streamlit run d:/Python/Streamlit/StockPrice.py
"""