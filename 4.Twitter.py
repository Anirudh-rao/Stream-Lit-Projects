import pandas as pd
import streamlit as st

st.title("Welcome to my Twitter Analysis")
st.write( "## Hello ##")

with st.container():
   df =  pd.read_csv("Data/twitter_training.csv")
   st.dataframe(df)

st.write("This is the Dataset we are working on")
