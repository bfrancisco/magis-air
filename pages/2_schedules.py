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
    db_cols = "departure_time, arrival_time, flight_cost, flight_code"
    query.append(
        db.query(f"SELECT {db_cols} FROM flight_schedule fs LEFT JOIN route rt ON fs.route_id = rt.route_id WHERE {where1} AND {where2} AND {where3}", ttl="1min").to_dict()
    )

clean_query = []
for i in range(7):
    cq_lst = [{"departure_time" : None, "arrival_time" : None, "flight_cost" : None, "flight_code": None} for j in range(len(query[i]["departure_time"]))]

    for k, v_dict in query[i].items():
        ind = 0
        for grbg, v in v_dict.items():
            cq_lst[ind][k] = v
            ind += 1

    clean_query.append(cq_lst)

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
        db_day = clean_query[i]

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


