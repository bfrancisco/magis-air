import streamlit as st
import datetime

# Filter flight schedules based on session_state data
# sql query filter:
#   - departure_date + 6days
#   - pref_time + 3hrs
#   - duration
#   - origin
#   - destination
# 
# output, table containing:
#   - departure_date
#   - departure_time
#   - duration
#   - arrival_time
#   - flight_code

temp_query = [
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=1),
            "departure_time" : datetime.time(hour=1, minute=30),
            "duration" : 120,
            "arrival_time" : datetime.time(hour=3, minute=30),
            "flight_code" : "ABC-001"
        },
        {
            "departure_date" : datetime.date(year=2024, month=1, day=1),
            "departure_time" : datetime.time(hour=3, minute=30),
            "duration" : 120,
            "arrival_time" : datetime.time(hour=5, minute=30),
            "flight_code" : "ABC-002"
        },
    ],
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=2),
            "departure_time" : datetime.time(hour=4, minute=0),
            "duration" : 180,
            "arrival_time" : datetime.time(hour=7, minute=0),
            "flight_code" : "ABC-003"
        },
    ],
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=2),
            "departure_time" : datetime.time(hour=4, minute=0),
            "duration" : 60,
            "arrival_time" : datetime.time(hour=5, minute=0),
            "flight_code" : "ABC-004"
        },
    ],
    [],[],[],[],

]

h_col1, h_col2 = st.columns([5.77, 1], vertical_alignment="bottom")
with h_col1:
    st.header("Available Flights")
with h_col2:
    if st.button("🔙 Return"):
        st.switch_page("pages/1_destination.py")

days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
day_ofthe_week = st.session_state["pref_date"].weekday()   # int. 0 - Monday, 1 - Tuesday, ...
for i in range(7):
    if day_ofthe_week == i:
        break
    days.append(days.pop(0))

pref_date = st.session_state["pref_date"]
tabs = st.tabs([f'{days[i]}, {(pref_date + datetime.timedelta(days=i)).strftime("%b %d")}' for i in range(7)])

for i in range(7):
    with tabs[i]:
        db_day = temp_query[i]

        if len(db_day) == 0:
            st.write("😢 No available flights for this date.")
            continue
        
        for db in db_day:
            with st.container(border=True):
                cols = st.columns([4.7, 1, 1], vertical_alignment="center")
                with cols[0]:
                    st.write(f'✈️ **{st.session_state["origin"]} to {st.session_state["destination"]}**')
                    
                    st.write(f'🕒 {db["departure_time"].strftime("%H:%M")} - {db["arrival_time"].strftime("%H:%M")} UTC')
                with cols[-2]:
                    st.write("PHP 2,000.00")
                with cols[-1]:
                    if st.button("🛫 Book", key=db["flight_code"]):
                        # put relevant data to st.session_state
                        st.switch_page("pages/3_passenger.py")


