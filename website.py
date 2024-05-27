import streamlit as st
import sqlite3
from databases import databases_setup
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
            st.success("Registration successful!")# Function to display the Form pages

def form_page():
    st.title("Form Page")
    st.write("Please fill out the form below:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=100)
    submit = st.button("Submit")
    
    if submit:
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")

# Function to display the Dashboard page
def dashboard_page():
    st.title("Dashboard")
    st.write("This is the dashboard page. Here you can display various data visualizations and metrics.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Welcome", "Form", "Dashboard"])

# Display the selected page
if page == "Welcome":
    welcome_page()
elif page == "Form":
    form_page()
elif page == "Dashboard":
    dashboard_page()

