import streamlit as st
import sqlite3


def providers_form(active_user_email):
    st.title("Provider Form Page")
    st.write("Please fill out the form below:")

    # Create a form for the inputs
    with st.form("customer_form"):

        company_name = st.text_input("Company name:", placeholder="Best Solar Panels Praha")
        company_DUNS = st.text_input("Company D-U-N-S code:", placeholder="15-048-3782 / 150483782")
        company_website = st.text_input("Company website:", placeholder="solarsolutions.com")

        st.subheader("Warehouse Address")
        provider_address_col1, provider_address_col2 = st.columns(2)

        with provider_address_col1:
            provider_city = st.text_input("City:", placeholder="Praha")

        with provider_address_col2:
            provider_street = st.text_input("Street and number:", placeholder="Kolbenova 9")

        # Product Information
        st.subheader("Product offers")
        price_per_panel = st.number_input("Price per PV panel:", placeholder="Price in CZK for a standard panel")
        heatpump_price = st.number_input("Price for one heat pump:", placeholder="Price in CZK for a standard heat pump")
        battery_price = st.number_input("Price for one house battery:", placeholder="Price in CZK for a standard battery ")
        charger_price = st.number_input("Price for one car charger:", placeholder="Price in CZK for a standard car charger")

        st.subheader("Pransportation Information")
        transport_price_per_km = st.number_input("Hardware transportation price per KM:", placeholder="Price in CZK for one KM of distance")

               # Submit Button
        submit_client_form = st.form_submit_button(label="Submit")
        
        if submit_client_form:
            empty_field = None
            if not provider_city:
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
                provider_address = provider_city + " " + provider_street
                coordinates = get_coordinates(provider_address)
                solar_data = get_solar_data(coordinates)
                add_client_info(active_user_email, provider_address, current_energy_consumption, solar_data["max_panels_area"], ev_option)
                
                st.success("Data submitted successfuly!")
                user_dashboard(active_user_email)

