import streamlit as st
import datetime

temp_cities = [
    "Manila",
    "Gensan",
    "Cebu",
]

def compute_time(a):
    "only accepts string formatted time (HH:MM)"
    a_hm = a.split(":")
    a_val = int(a_hm[0])*60 + int(a_hm[1])
    return a_val

orgn_col, dest_col = st.columns(2)
with orgn_col:
    origin = st.selectbox(
        "Select origin",
        (temp_cities),
    )
with dest_col:
    destination = st.selectbox(
        "Select destination",
        (temp_cities),
    )

date_col, time_col = st.columns(2)
with date_col:
    departure_date = st.date_input("Select preferred departure date", value="today")
with time_col:
    departure_time = st.time_input("Select preferred departure time (UTC)", value=None)

if st.button("**📃 Check available flights**", use_container_width=True):
    if origin == None or destination == None or departure_date == None or departure_time == None:
        st.error("Please fill out all fields.", icon="🚨")
    elif origin == destination:
        st.error("Your origin and destination cannot be the same.", icon="🚨")
    elif departure_date < datetime.date.today():
        st.error("Please choose a later departure date.", icon="🚨")
    elif departure_date == datetime.date.today() and compute_time(str(departure_time)) < compute_time(datetime.datetime.now().strftime("%H:%M")) + 120:
        st.error("Please choose a later departure time.", icon="🚨")

    else:
        st.session_state["origin"] = origin
        st.session_state["destination"] = destination
        st.session_state["pref_date"] = departure_date
        st.session_state["pref_time"] = departure_time

        st.switch_page("pages/2_schedules.py")