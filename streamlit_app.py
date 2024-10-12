import streamlit as st

st.title("Anomaly Detection SG Mapper")

dimension1 = st.selectbox(
    "Choose your first dimension?",
    ('location', 'Home phone', 'Mobile phone'))

dimension2 = st.selectbox(
    "Choose your second dimension?",
    ('location', 'Home phone', 'Mobile phone'))

st.write(f"You selected:, {dimension1} and {dimension2}")