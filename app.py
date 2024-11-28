import datetime


st.title("Magis Air ✈️")

pg = st.navigation([
    st.Page("pages/1_destination.py", title="Magis Air | Select Destination", icon="✈️"),
    st.Page("pages/2_schedules.py", title="Magis Air | Flight Schedules", icon="✈️"),
    st.Page("pages/3_passenger.py", title="Magis Air | Passenger Info", icon="✈️"),
    st.Page("pages/4_booking.py", title="Magis Air | Flight Booking", icon="✈️"),
])
pg.run()