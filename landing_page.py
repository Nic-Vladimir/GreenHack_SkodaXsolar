import streamlit as st
from database.database import *
from database.database_utils import *
from clients.client_form import *
from clients.client_dashboard import *
from admins.admin_dashboard import *
from providers.providers_form import *

# Function to display the Welcome page
def landing_page():
    # Create two columns
    col1, col2 = st.columns(2)
    
    # First column content
    with col1:
        st.title("Welcome")
        st.write("""At SkodaX, we understand the importance of making sustainable choices for a greener future. Our platform is dedicated to helping you navigate the world of sustainable technologies, with a particular focus on photovoltaic panels. We aim to provide you with the knowledge and tools necessary to make informed decisions that benefit both your wallet and the environment.
Connect with Trusted Providers

Our platform offers a seamless connection between clients and sustainable technology providers. Whether you're looking for solar panels, heat pumps, house batteries,""")
    
    # Second column content
    with col2:
        st.title("User Registration")
        st.write("Sign up and let's explore the benefits of solar energy!")

        with st.form(key="initial_user_registration"):

            # Account type selection
            user_type = st.selectbox("Which best describes you?", ["Client", "Provider", "Admin"])

            # User info
            email = st.text_input("Email", placeholder="john.doe@gmail.com")
            password = st.text_input("Password", type="password", placeholder="Create a password")
            password_re = st.text_input("Password", type='password', placeholder="Re-enter password")

            # Submit button
            sign_up = st.form_submit_button(label="Sign up")

        if sign_up:
            empty_field = None
            if not email:
                empty_field = "Email"
            elif not password:
                empty_field = "Password"
            elif not password_re:
                empty_field = "Confirm Password"
            elif password != password_re:
                empty_field = "Passwords do not match"

            if empty_field:
                st.error(f"Please complete the following field: {empty_field}")
            else:
                if user_type == "Client":
                    register_client(email, password)
                    st.success("Registration successful!")
                    client_form(email)
                elif user_type == "Provider":
                    register_provider(email, password)
                    st.success("Registration successful!")
                    providers_form(email)
                elif user_type == "Admin":
                    register_admin(email, password)
                    st.success("Registration successful!")
                    admin_dashboard(email)


        with st.expander("Or Login if you have an account! :)", expanded=False):
            with st.form(key="user_login"):
                # Login form elements
                email = st.text_input("Email", placeholder="john.doe@gmail.com")
                password = st.text_input("Password", type="password", placeholder="password123")
                login_button = st.form_submit_button(label="Log In")

                # Logic for login button press (replace with your actual authentication logic)
                if login_button:
                    table, active_user_email = check_login(email, password)

                    if table == "admins":
                        st.success("Login successful!")
                        admin_dashboard(active_user_email )

                    elif table == "clients":
                        st.success("Login successful!")
                        client_dashboard(active_user_email )

                    elif table == "providers":
                        st.success("Login successful!")
                        providers_form(active_user_email )

