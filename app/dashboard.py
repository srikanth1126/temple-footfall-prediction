import streamlit as st
import pandas as pd

st.title("Temple Footfall Dashboard")
data = pd.read_csv("data/sample_data.csv")
st.line_chart(data['footfall'])
