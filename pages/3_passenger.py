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
    last_name = st.text_input("Last name")
with name_cols[1]:
    first_name = st.text_input("First name")
with name_cols[2]:
    middle_name = st.text_input("Middle name")

birth_date = st.date_input("Birthdate", value=datetime.datetime(2004, 1, 1))

gender = st.selectbox(
    "Gender",
    ["Female", "Male", "Nonbinary", "Prefer not to say"],
)

def display_item_input(index):
    left, right = st.columns([5, 1])
    left.text_input('Item name', key=f'name_{index}')
    right.number_input('Weight in kg', key=f'kg_{index}', min_value=0)

if 'item_rows' not in st.session_state:
    st.session_state['item_rows'] = 1

def increase_rows():
    st.session_state['item_rows'] += 1

item_head_cols = st.columns([5, 1], vertical_alignment="bottom")
item_head_cols[0].header("Additional Items")
item_head_cols[1].button("➕ Add row", on_click=increase_rows)
item_container = st.container()


with item_container:
    for i in range(st.session_state['item_rows']):
        display_item_input(i)

if st.button("➡️ Proceed to Booking Confirmation", use_container_width=True):    
    if first_name == "" or last_name == "" or middle_name == "":
        pass
    else:
        st.session_state['first_name'] = first_name
        st.session_state['last_name'] = last_name
        st.session_state['middle_name'] = middle_name
        st.session_state['birthdate'] = birth_date
        st.session_state['gender'] = gender
        st.session_state.pop('pref_date')
        st.session_state.pop('pref_time')
        valid_rows = 0
        for i in range(st.session_state['item_rows']):
            if st.session_state[f'name_{i}'] == "":
                continue
            st.session_state[f'item_name_{valid_rows}'] = st.session_state[f'name_{i}']
            st.session_state[f'item_kg_{valid_rows}'] = st.session_state[f'kg_{i}']
            valid_rows += 1
        st.session_state['item_rows'] = valid_rows
        st.switch_page("pages/4_booking.py")