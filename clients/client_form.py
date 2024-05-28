import streamlit as st
import sqlite3

# ----Page Config----
st.set_page_config(page_title="Škoda - Opti:Energy", page_icon="🌤", layout="wide")

# Function to display the Welcome page
def welcome_page():
    # Create two columns
    col1, col2 = st.columns(2)

    # First column content
    with col1:
        st.title("Welcome")
        st.write("Welcome to the Streamlit application. Use the sidebar to navigate through the pages.")

    # Second column content
    with col2:
        st.title("User Registration")
        st.write("Please fill out the registration form:")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        register = st.button("Register")

        if register:
            st.write(f"Username: {username}")
            st.write(f"Email: {email}")
            st.success("Registration successful!")

# Function to check for unfilled fields
def check_for_unfilled_fields(*fields):
    missing_fields = [field for field in fields if not field]
    if missing_fields:
        st.error("Fill out all the goddamn fields for fuck sake!!")
        return False
    return True

def form_page():
    st.title("Customer Form Page")
    st.write("Please fill out the form below:")

    # Create a form for the inputs
    with st.form("customer_form"):
        # User Information Section
        st.subheader("Personal Information")
        customer_firstname = st.text_input("Your first name:", placeholder="Justin")
        customer_lastname = st.text_input("Your last name:", placeholder="Bober")
        customer_email = st.text_input("Your email:", placeholder="some@fuckery.gg")
        st.subheader("Phone Number")

        # Create a horizontal layout for country code and phone number
        phone_number_col1, phone_number_col2 = st.columns([1, 2])

        # Input field for country code
        with phone_number_col1:
            phone_country_code = st.text_input("Country Code", max_chars=3)

        # Input field for phone number
        with phone_number_col2:
            phone_number = st.text_input("Phone Number", max_chars=9)

        # Combine the parts into a single phone number string
        full_phone_number = f"+{phone_country_code}-{phone_number}" if phone_country_code and phone_number else ""

        # Address Section
        st.subheader("Address Information")
        user_address_col1, user_address_col2, user_address_col3 = st.columns([1, 2, 1])

        with user_address_col1:
            customer_city = st.text_input("Your city:", placeholder="New York")

        with user_address_col2:
            customer_street = st.text_input("Your street:", placeholder="5th Avenue")

        with user_address_col3:
            customer_zip = st.text_input("Your zip:", placeholder="10001")

        # Energy Provider and Consumption Information
        st.subheader("Energy Information")
        customer_current_energy_provider = st.text_input("Current Energy Provider")
        customer_current_energy_consumption = st.number_input("Current Energy Consumption (in KWh)", min_value=0)
        customer_current_energy_peak_power = st.number_input("Current Energy Peak Power (in KW)", min_value=0)
        customer_current_energy_cost = st.number_input("Current Energy Cost (in CZK)", min_value=0)
        customer_possible_energy_consumption = st.number_input("Possible Energy Consumption (in KWh)", min_value=0)
        customer_possible_energy_cost = st.number_input("Possible Energy Cost (in CZK)", min_value=0)

        # Preferences Section
        st.subheader("Preferences")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.write("Electric Vehicle")
            electric_vehicle_option = st.selectbox("", ["I have", "I want", "I don't want"], key="ev_option")

        with col2:
            st.write("Heat Pump")
            heat_pump_option = st.selectbox("", ["I have", "I want", "I don't want"], key="hp_option")

        with col3:
            st.write("Solar Panels")
            solar_panels_option = st.selectbox("", ["I have", "I want", "I don't want"], key="sp_option")

        with col4:
            st.write("Battery")
            battery_option = st.selectbox("", ["I have", "I want", "I don't want"], key="bt_option")

        # Submit Button
        submit = st.form_submit_button("Submit")

&a
