# helper.py

import streamlit as st

def kpi_card(title, value, bg_color="#F9F9F9"):
    card_html = f"""
    <div style="
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        color: #333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <h4 style="margin-bottom: 10px; color: {bg_color};">{title}</h4>
        <p style="font-size: 16px; font-weight: bold; margin: 0; color: {bg_color};">{value}</p>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
