# app.py
import streamlit as st


# Page config
st.set_page_config(
    page_title="Bank Customer Attrition Predictor",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Importing the pages
from page.prediction import prediction
from page.dashboard import dashboard

# Setting the sidebar
page = st.sidebar.selectbox("Attrition Project", ["Prediction", "Dashboard"])

if page == "Prediction":
    prediction()
elif page == "Dashboard":
    dashboard()
else:
    raise "Unknown"
