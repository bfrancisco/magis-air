import streamlit as st
import datetime

temp_cities = [
    "Manila",
    "Gensan",
    "Cebu",
]

origin = st.selectbox(
    "Select origin",
    (temp_cities)
)

destination = st.selectbox(
    "Select destination",
    (temp_cities)
)

departure_date = st.date_input("Select preferred departure date", value=None)

departure_time = st.time_input("Select preferred departure time", value=None)

if st.button("Check available flights"):
    st.switch_page("pages/2_schedules.py")