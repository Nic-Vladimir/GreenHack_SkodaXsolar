import streamlit as st
import sqlite3


# Function to check for unfilled fields
def check_for_unfilled_fields(*fields):
    missing_fields = [field for field in fields if not field]
    if missing_fields:
        st.error("Fill out all the fields!")
        return False
    return True

def client_form(active_user_email):
    st.title("Customer Form Page")
    st.write("Please fill out the form below:")

    # Create a form for the inputs
    with st.form("customer_form"):


        st.subheader("Address Information")
        user_address_col1, user_address_col2 = st.columns(2)

        with user_address_col1:
            client_city = st.text_input("City:", placeholder="Praha")

        with user_address_col2:
            client_street = st.text_input("Street and number:", placeholder="Kolbenova 9")


        # Energy Information
        st.subheader("Energy Information")
        #customer_current_energy_provider = st.text_input("Current Energy Provider")
        current_energy_consumption = st.number_input("Average Monthly Energy Consumption (in KWh)", placeholder="Check your last invoice")
        current_energy_cost = st.number_input("Average Monthly Energy Cost (in CZK)", placeholder="Check your last invoice")

        # Preferences Section
        st.subheader("Preferences")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            ev_option = st.selectbox("Electric Vehicle", ["I have", "I want", "I don't want"], key="ev_option")

        with col2:
            heat_pump_option = st.selectbox("Heat Pump", ["I have", "I want", "I don't want"], key="hp_option")

        with col3:
            solar_panels_option = st.selectbox("Solar Panels", ["I have", "I want", "I don't want"], key="sp_option")

        with col4:
            #st.write("Battery")
            battery_option = st.selectbox("Battery", ["I have", "I want", "I don't want"], key="bt_option")

        # Submit Button
        submit_client_form = st.form_submit_button(label="Submit")
        
        if submit_client_form:
            empty_field = None
            if not client_city:
                empty_field = "Adress: City"
            elif not client_street:
                empty_field = "Adress: Street and number"
            elif not current_energy_consumption:
                empty_field = "Current Consumption"
            elif not current_energy_cost:
                empty_field = "Current Cost"


            if empty_field:
                st.error(f"Please complete the following field: {empty_field}")
            else:
                user_address = client_city + " " + client_street
                coordinates = get_coordinates(user_address)
                solar_data = get_solar_data(coordinates)
                add_client_info(active_user_email, user_address, current_energy_consumption, solar_data["max_panels_area"], ev_option)
                
                st.success("Data submitted successfuly!")
                user_dashboard(active_user_email)

