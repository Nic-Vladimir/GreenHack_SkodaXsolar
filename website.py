import streamlit as st
import sqlite3
import landing_page
from database.database import *
from landing_page import *
from clients.client_form import *
from clients.client_dashboard import *


databases_setup()

# ----Page Config----
st.set_page_config(page_title="Škoda - Opti:Energy", page_icon="🌤", layout="wide")


landing_page()

# Function to display the Dashboard page
def dashboard_page():
    st.title("Dashboard")
    st.write("This is the dashboard page. Here you can display various data visualizations and metrics.")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("", ["Welcome", "Form", "Dashboard"])

# Display the selected page
if page == "Form":
    clients.client_form()
elif page == "Dashboard":
    clients.client_dashboard()



