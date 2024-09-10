import pandas
import streamlit as st

st.title("💗 Dating Match Predictor 💗")

st.sidebar.header("Please fill out the information below")
st.sidebar.selectbox("Pick your gender", ["Male","Female"])
st.sidebar.selectbox("Did you purchase a VIP account", ["No","Yes"])
st.sidebar.slider("Please specify your income", 15000,30000)
st.sidebar.selectbox("How many children do you have", [0,1,2,3,4,5,6])
st.sidebar.slider("How would you rate your attractiveness",0,10)
st.sidebar.button("Submit")

