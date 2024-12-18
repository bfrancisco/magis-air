import streamlit as st

db = st.session_state["db"]

head = st.columns(3)
with head[0]:
    if st.button("🔙 Return", use_container_width=True):
        st.switch_page("pages/1_destination.py")


name_cols = st.columns(3)
with name_cols[0]:
    last_name = st.text_input("Last name")
with name_cols[1]:
    first_name = st.text_input("First name")
with name_cols[2]:
    middle_name = st.text_input("Middle name")

if st.button("📃 Show Booked Flights", use_container_width=True):
    if last_name == "" or first_name == "" or middle_name == "":
        st.error("Please fill out all fields.", icon="🚨")
    else:
        q_passenger_info = f"""
        select distinct pa.last_name as "Last Name", pa.first_name as "First Name", pa.middle_name as "Middle Name", pa.birth_date as "Birthdate", pa.gender as "Gender"
        from booking bk
        LEFT JOIN passenger pa ON bk.passenger_id=pa.passenger_id 
        WHERE pa.first_name ILIKE '{first_name}' AND pa.middle_name ILIKE '{middle_name}' AND pa.last_name ILIKE '{last_name}';
        """

        q_trip_itinerary = f"""
        select fs.flight_code as "Flight Code", co.name as "Origin", cd as "Destination", fs.departure_time as "Departure", fs.arrival_time as "Arrival", fs.duration as "Duration", fs.flight_cost as "Cost", bk.booking_date as "Passenger Booking Date", bk.total_cost as "Passenger Total Cost"
        from booking bk 
        LEFT JOIN passenger pa ON bk.passenger_id=pa.passenger_id 
        LEFT JOIN flight_schedule fs ON bk.flight_code=fs.flight_code 
        LEFT JOIN route rt ON fs.route_id=rt.route_id 
        LEFT JOIN city co ON rt.city_origin=co.name 
        LEFT JOIN city cd ON rt.city_destination=cd.name
        WHERE pa.first_name ILIKE '{first_name}' AND pa.middle_name ILIKE '{middle_name}' AND pa.last_name ILIKE '{last_name}';
        """
        q_addtl_items = f"""
        select ai.item_name as Description, bkai.qty as Qty, (ai.cost*bkai.qty) as Cost 
        from booking bk 
        LEFT JOIN passenger pa ON bk.passenger_id=pa.passenger_id 
        LEFT JOIN booking_additional_item bkai ON bk.booking_id=bkai.booking_id
        LEFT JOIN additional_item ai ON bkai.item_no=ai.item_no
        WHERE pa.first_name ILIKE '{first_name}' AND pa.middle_name ILIKE '{middle_name}' AND pa.last_name ILIKE '{last_name}';
        """

        passenger_info = db.query(q_passenger_info)
        trip_itinerary = db.query(q_trip_itinerary)
        # addtl_items = db.query(q_addtl_items)

        st.subheader("Passenger Info")
        passenger_info
        st.subheader("Trip Itinerary")
        trip_itinerary
        # st.subheader("Additional Items")
        # addtl_items
