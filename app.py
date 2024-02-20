import streamlit as st
import pandas as pd

st.title("Esto es un título")
st.header("Esto es un header")
st.markdown("*italic*")

df = pd.read_csv("train.csv")
st.dataframe(df)

