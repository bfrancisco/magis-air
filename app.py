import streamlit as st
import datetime

db = st.connection("postgresql", type="sql")
st.session_state["db"] = db

st.title("Magis Air ✈️")

pg = st.navigation([
    st.Page("pages/1_destination.py", title="Magis Air | Select Destination", icon="✈️"),
    st.Page("pages/2_schedules.py", title="Magis Air | Flight Schedules", icon="✈️"),
    st.Page("pages/3_passenger.py", title="Magis Air | Passenger Info", icon="✈️"),
    st.Page("pages/4_booking.py", title="Magis Air | Flight Booking", icon="✈️"),
    st.Page("pages/5_summary.py", title="Magis Air | Booking Summary", icon="✈️"),
])
pg.run()