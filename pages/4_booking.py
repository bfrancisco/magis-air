import streamlit as st
import pandas as pd

db = st.session_state["db"]

st.session_state

flight_data = db.query(f'SELECT departure_time, arrival_time, departure_date, flight_cost FROM flight_schedule WHERE flight_code = {st.session_state["flight_code"]}').to_dict()

flight_data

db_front = {
    "Name" : f'{st.session_state["last_name"]}, {st.session_state["first_name"]} {st.session_state["middle_name"][0]}.',
    "Birthdate" : st.session_state["birthdate"].strftime("%B %d, %Y"),
    "Gender" : st.session_state["gender"],
    "Origin City" : st.session_state["origin"],
    "Destination City" : st.session_state["destination"],
    "Departure Date" : flight_data["departure_date"][0].strftime("%B %d, %Y"),
    "Departure Time" : f'{flight_data["departure_time"][0].strftime("%H:%M")} UTC',
    "Arrival Time" : f'{flight_data["arrival_time"][0].strftime("%H:%M")} UTC',
    "Flight Cost" : f'PHP {"{:.2f}".format(flight_data["flight_cost"][0])}',
}
addtl_items = [
        "Additional Baggage Allowance (5kg)", 
        "Teriminal Fees", 
        "Travel Insurance"
    ]

availed_items = {} # item : {cost : #, qty : #}

total_cost = flight_data["flight_cost"][0]

for itm in addtl_items:
    if not st.session_state[f'item_avail_{itm}'] or st.session_state[f'item_qty_{itm}'] == 0:
        continue
    shrt_itm = "Addtl. Baggage Allowance" if itm == "Additional Baggage Allowance (5kg)" else itm
    itm_cost = float((st.session_state[f'item_price_{itm}'].split())[1]) * st.session_state[f'item_qty_{itm}']
    db_front[f'{shrt_itm} Qty and Total Cost'] = f"{st.session_state[f'item_qty_{itm}']} pc{'s' if st.session_state[f'item_qty_{itm}'] > 1 else ''}, {'PHP ' + '{:.2f}'.format(itm_cost)}"
    total_cost += itm_cost

db_front["Total Cost"] = f"{'PHP ' + '{:.2f}'.format(total_cost)}"



st.header("Confirm Flight Booking")

cols = st.columns(2)

for key, value in db_front.items():
    cols[0].write(f'**{key}**')
    cols[1].write(str(value))


