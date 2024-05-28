import streamlit as st
import sqlite3


# Function to approve a company
def approve_company(company_id):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE providers SET status = 'Approved' WHERE id = ?", (company_id,))
        conn.commit()
        st.success(f"Company with ID {company_id} approved")
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        conn.close()


# Function to disapprove a company
def rejected_company(company_id, reason):
    try:
        conn = sqlite3.connect('admin_page.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE service_companies SET status = 'Rejected', reason_rejected = ? WHERE id = ?", (reason, company_id))
        conn.commit()
        st.warning(f"Company with ID {company_id} :red[rejected] because: _{reason}_")
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
    finally:
        conn.close()


# Function to get service companies
def get_service_companies(status):
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if status == "All":
            cursor.execute("SELECT * FROM service_companies")
            companies = cursor.fetchall()
            return companies

        cursor.execute("SELECT * FROM service_companies WHERE status = ?", status)
        companies = cursor.fetchall()
        return companies
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

def admin_dashboard(active_user_email):
    companies = st.selectbox("What companies to display?", ("All", "Pending", "Approved", "Rejected"))
    if companies == "Pending":
        st.title("Service companies waiting for approval")
    companies = get_service_companies(companies)
    for i, company in enumerate(companies):
        with st.container(border=True):
            col1, col2 = st.columns(2)
            with col1:
                company_id = company["id"]
                st.write(f"Name: {company["company_name"]}")
                st.write(f"Code: {company["company_DUNS"]}")
                st.write(f"Website: {company["company_website"]}")
                st.write(f"Warehouse Address: {company["warehouse_address"]}")
                st.write(f"E-mail: {company["email"]}")
                with st.expander("Extra Details", expanded=False):
                    st.write(f"Panel Price: {company["company_panelprice"]}")
                    st.write(f"Heat Pump Price: {company["company_heatpumpprice"]}")
                    st.write(f"Battery Price: {company["company_batterprice"]}")
                    st.write(f"Charger Price: {company["company_chargerprice"]}")
                    st.write(f"Transport Price: {company["company_transportprice"]}")

            with col2:
                st.button("Approve", key=f"approve_{company_id}", on_click=approve_company(company_id,))
                rejected_reason = st.text_input("Reason (required for disapproval)", key=f"reason_{company_id}")
                st.button("Reject", key=f"rejected_{company_id}", on_click=rejected_company(company_id, rejected_reason))

