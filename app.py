import streamlit as st
import numpy as np
import pickle

st.title("Customer Churn Prediction App")

st.write("Enter customer details below:")

# Inputs
tenure = st.number_input("Tenure (months)", 0, 100, 12)
monthly_charges = st.number_input("Monthly Charges", 0, 200, 70)
total_charges = st.number_input("Total Charges", 0, 10000, 1000)

# Simple logic placeholder (we will improve later with model)
if st.button("Predict Churn"):
    if tenure < 12 and monthly_charges > 70:
        st.error("Customer is likely to CHURN")
    else:
        st.success("Customer is likely to STAY")
