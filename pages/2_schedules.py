import streamlit as st
import datetime

db = st.session_state["db"]

# Filter flight schedules based on session_state data
# sql query filter:
#   - departure_date + 6days (query per day)
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

days = ["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"]
day_ofthe_week = st.session_state["pref_date"].weekday()   # int. 0 - Monday, 1 - Tuesday, ...
for i in range(7):
    if day_ofthe_week == i:
        break
    days.append(days.pop(0))

query = []
for i in range(7):
    where1 = f"DATE'{st.session_state['pref_date'] + datetime.timedelta(days=i)}' = departure_date"
    time_obj = datetime.time(hour=(st.session_state['pref_time'].hour + 2)%24, minute=st.session_state['pref_time'].minute)
    where2 = f"TIME'{time_obj}' <= departure_time"
    where3 = f"city_origin LIKE '{st.session_state['origin']}' AND city_destination LIKE '{st.session_state['destination']}'"
    db_cols = "departure_time, arrival_time, flight_cost"
    query.append(
        db.query(f"SELECT {db_cols} FROM flight_schedule fs LEFT JOIN route rt ON fs.route_id = rt.route_id WHERE {where1} AND {where2} AND {where3}").to_dict()
    )

query[0]
print(query[0].items())
for k, v in query[0].items():
    st.write(k)
    st.write(v)

clean_query = [[] for i in range(7)]
for i in range(7):
    
    for k, v_dict in query[i].items():
        dct = {"departure_date" : None, "departure_time" : None, "arrival_time" : None, "flight_code" : None}
        
        for key in range(len(query[i]["departure_time"])):
            dct[k]
        
    
    v["departure_time"]["0"]

temp_query = [
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=1),
            "departure_time" : datetime.time(hour=1, minute=30),
            "arrival_time" : datetime.time(hour=3, minute=30),
            "flight_code" : "ABC-001"
        },
        {
            "departure_date" : datetime.date(year=2024, month=1, day=1),
            "departure_time" : datetime.time(hour=3, minute=30),
            "arrival_time" : datetime.time(hour=5, minute=30),
            "flight_code" : "ABC-002"
        },
    ],
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=2),
            "departure_time" : datetime.time(hour=4, minute=0),
            "arrival_time" : datetime.time(hour=7, minute=0),
            "flight_code" : "ABC-003"
        },
    ],
    [
        {
            "departure_date" : datetime.date(year=2024, month=1, day=2),
            "departure_time" : datetime.time(hour=4, minute=0),
            "arrival_time" : datetime.time(hour=5, minute=0),
            "flight_code" : "ABC-004"
        },
    ],
    [],[],[],[],

]

h_col1, h_col2 = st.columns([5.5, 1], vertical_alignment="bottom")
with h_col1:
    st.header("Available Flights")
with h_col2:
    if st.button("🔙 Return"):
        st.switch_page("pages/1_destination.py")

pref_date = st.session_state["pref_date"]
tabs = st.tabs([f'{days[i]}, {(pref_date + datetime.timedelta(days=i)).strftime("%b %d")}' for i in range(7)])

for i in range(7):
    with tabs[i]:
        db_day = temp_query[i]

        if len(db_day) == 0:
            st.write("😢 No available flights for this date.")
            continue
        
        for db_query in db_day:
            with st.container(border=True):
                cols = st.columns([4.7, 1, 1], vertical_alignment="center")
                with cols[0]:
                    st.write(f'✈️ **{st.session_state["origin"]} to {st.session_state["destination"]}**')
                    
                    st.write(f'🕒 {db_query["departure_time"].strftime("%H:%M")} - {db_query["arrival_time"].strftime("%H:%M")} UTC')
                with cols[-2]:
                    st.write("PHP 2,000.00")
                with cols[-1]:
                    if st.button("🛫 Book", key=db_query["flight_code"]):
                        # put relevant data to st.session_state
                        st.switch_page("pages/3_passenger.py")


