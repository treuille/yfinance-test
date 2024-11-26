import streamlit as st
import yfinance

# Simple confirmation message to prove the module was imported successfully
st.title("YFinance Import Test")
st.text(f"YFinance module imported successfully! Version: {yfinance.__version__}")