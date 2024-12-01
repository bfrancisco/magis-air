import streamlit as st
import pandas as pd
import datetime
from sqlalchemy import text

db = st.session_state["db"]

flight_data = db.query(f'SELECT departure_time, arrival_time, departure_date, flight_cost FROM flight_schedule WHERE flight_code = {st.session_state["flight_code"]}').to_dict()

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


total_cost = flight_data["flight_cost"][0]


for itm in st.session_state['item_names']:
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

def create_passenger(first_name, middle_name, last_name, date, gender):
    # date should be in 'YYYY-MM-DD' format as a string
    db.query(f"INSERT INTO passenger (first_name, middle_name, last_name, birth_date, gender) VALUES ('{first_name}', '{middle_name}', '{last_name}', DATE '{date}', '{gender}');")
    st.write("Created passenger data.")

def create_booking(date, tot_cost, passenger_id, flight_code):
    # date should be in 'YYYY-MM-DD' format as a string
    db.query(f"INSERT INTO booking (booking_date, total_cost, passenger_id, flight_code) VALUES (DATE '{date}', {tot_cost}, {passenger_id}, {flight_code})")
    st.write("Created booking data.")

def create_book_item(booking_id, item_no, qty):
    db.query(f"INSERT INTO booking_additional_item (booking_id, item_no, qty) VALUES ({booking_id}, {item_no}, {qty});")
    st.write("Created booking_item data.")

if st.button("✅ Confirm booking", use_container_width=True):
    # Create Passenger
    # Create Booking connecting to: passenger, flight_schedule
    # Create associative booking -- addtl_item
    with db.session as session:
        result_passenger = session.execute(
            text("INSERT INTO passenger (first_name, middle_name, last_name, birth_date, gender) VALUES (:first_name, :middle_name, :last_name, :birthdate, :gender) RETURNING passenger_id;"),
            params=dict(
                first_name=st.session_state['first_name'], 
                middle_name=st.session_state['middle_name'], 
                last_name=st.session_state['last_name'], 
                birthdate=st.session_state['birthdate'], 
                gender=st.session_state['gender']
            )
        )
        new_passenger_id = result_passenger.scalar_one()

        result_booking = session.execute(
            text("INSERT INTO booking (booking_date, total_cost, passenger_id, flight_code) VALUES (:booking_date, :tot_cost, :passenger_id, :flight_code) RETURNING booking_id;"),
            params=dict(booking_date=datetime.datetime.now().date(), tot_cost=total_cost, passenger_id=new_passenger_id, flight_code=st.session_state['flight_code'])
        )
        new_booking_id = result_booking.scalar_one()

        for k in st.session_state['item_names']:
            session.execute(
                text("INSERT INTO booking_additional_item (booking_id, item_no, qty) VALUES (:book_id, :item_id, :qty)"),
                params=dict(book_id=new_booking_id, item_id=st.session_state[f'item_no_{k}'], qty=st.session_state[f'item_qty_{k}'])
            )

        session.commit()

        st.success("✅ Flight Booked!")
        st.balloons()

        # if st.button("🛫 Book another flight", use_container_width=True):
        #     for key in st.session_state.keys():
        #         if key=='db': continue
        #         del st.session_state[key]
        #     st.switch_page("pages/1_destination.py")

if st.button("🛫 Book another flight", use_container_width=True):
    for key in st.session_state.keys():
        if key=='db': continue
        del st.session_state[key]
    st.switch_page("pages/1_destination.py")