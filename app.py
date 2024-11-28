import datetime

import streamlit as st

st.title("Magis Air ✈️")

db = st.connection("postgresql", type="sql")

temp_cities = db.query("SELECT name FROM city;", ttl="1hr")

origin = st.selectbox("Select origin", (temp_cities))

destination = st.selectbox("Select destination", (temp_cities))

departure_date = st.date_input("Select preferred departure date", value=None)

departure_time = st.time_input("Select preferred departure time", value=None)

if st.button("Check flights"):
    st.write("EYY")
