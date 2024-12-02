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

def increase_rows():
    st.session_state['item_rows'] += 1

st.header("Additional Items")

addtl_items_query = db.query("SELECT * FROM additional_item;").to_dict()
item_cnt = len(addtl_items_query["item_no"])

addtl_items = {}
item_names = []

for i in range(item_cnt):
    addtl_items[addtl_items_query["item_name"][i]] = addtl_items_query["cost"][i]
    item_names.append(addtl_items_query["item_name"][i])

# addtl_items = {
#         "Additional Baggage Allowance (5kg)" : 237, 
#         "Teriminal Fees" : 273, 
#         "Travel Insurance" : 208,
#     }

for k, v in addtl_items.items():
    col1, col2, col3, col4 = st.columns([0.8, 3.7, 1.2, 0.8], vertical_alignment="center")
    col1.checkbox("Avail", key=f'avail_{k}')
    col2.text_input("Description", key=f'desc_{k}', disabled=True, value=k)
    col3.text_input("Price", key=f'price_{k}', disabled=True, value="PHP " + "{:.2f}".format(v))
    col4.number_input("Quantity", min_value=0, key=f'qty_{k}')

if st.button("➡️ Proceed to Booking Confirmation", use_container_width=True):    
    if first_name == "" or last_name == "":
        st.error("Please fill out all fields.", icon="🚨")
    else:
        st.session_state['first_name'] = first_name
        st.session_state['last_name'] = last_name
        st.session_state['middle_name'] = middle_name
        st.session_state['birthdate'] = birth_date
        st.session_state['gender'] = gender
        st.session_state.pop('pref_date')
        st.session_state.pop('pref_time')
        itm_no = 1
        for k, v in addtl_items.items():
            st.session_state[f'item_avail_{k}'] = st.session_state[f'avail_{k}']
            st.session_state[f'item_no_{k}'] = itm_no
            st.session_state[f'item_qty_{k}'] = st.session_state[f'qty_{k}']
            st.session_state[f'item_price_{k}'] = st.session_state[f'price_{k}']
            itm_no += 1
        st.session_state['item_count'] = item_cnt
        st.session_state['item_names'] = item_names
        
        st.switch_page("pages/4_booking.py")