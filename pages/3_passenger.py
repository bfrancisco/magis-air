import streamlit as st
import datetime

db = st.session_state["db"]

h_col1, h_col2 = st.columns([5.5, 1], vertical_alignment="bottom")
with h_col1:
    st.header("Passenger Details")
with h_col2:
    if st.button("🔙 Return"):
        st.switch_page("pages/2_schedules.py")

name_cols = st.columns(3) 
with name_cols[0]:
    st.text_input("Last name")
with name_cols[1]:
    st.text_input("First name")
with name_cols[2]:
    st.text_input("Middle name")

birth_date = st.date_input("Birthdate", value=datetime.datetime(2004, 1, 1))

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Nonbinary", "Prefer not to say"],
)

h_col1, h_col2 = st.columns([4.75, 1], vertical_alignment="bottom")
with h_col1:
    st.header("Additional Items")
with h_col2:
    if st.button("➕ Add Row"):
        st.write("add")

def add_item_input(btn_id):
        itemname = st.text_input("Item name")
    

if st.button("✅ Confirm", use_container_width=True):
    # put data to session_state
    st.switch_page("pages/4_booking.py")