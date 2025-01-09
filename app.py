import streamlit as st
import numpy as np
import joblib

st.title("Bike Purchasement Prediction App")

st.divider()

income = st.number_input("Enter the income", min_value=0, value=300)
age = st.number_input("Enter the age", min_value= 15, value=30)
educate = st.number_input("Enter the education", min_value= 0, value= 2)
homeowner = st.number_input("Home owner input", min_value=0, value=1)


joblib.load()













# 'Income', 'Age', 'Education', 'Home Owner' 