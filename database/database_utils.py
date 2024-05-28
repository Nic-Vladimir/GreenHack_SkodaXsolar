import sqlite3

# Function to connect to a database
def get_db_connection(db_name):
    conn = sqlite3.connect(f'{db_name}.db')
    return conn


# User registration
def register_client(fullname, client_email, password):
    conn = get_db_connection('clients')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clients (fullname, client_email, password)
        VALUES (?, ?, ?)
    ''', (fullname, client_email, password))
    conn.commit()
    conn.close()


# Function to update client info
def add_client_info(client_email, user_address, current_consumption, panel_area, vehicle):
    conn = get_db_connection('clients')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clients
        SET user_address = ?, current_consumption = ?, panel_area = ?, vehicle = ?
        WHERE client_email = ?
    ''', (user_address, current_consumption, panel_area, vehicle, client_email))
    conn.commit()
    conn.close()


def register_provider(username, email, password):
    conn = get_db_connection('providers')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO providers (username, email, password)
        VALUES (?, ?, ?)
    ''', (username, email, password))
    conn.commit()
    conn.close()


# Function to add a new provider
def add_provider(email, company_name, company_DUNS, company_website, warehouse_address, price_per_panel, heatpump_price, battery_price, charger_price, transport_price_per_km):
    conn = get_db_connection('providers')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE providers
        SET company_name = ?, company_DUNS = ?, company_website = ?, warehouse_address = ?, price_per_panel = ?, heatpump_price = ?, battery_price = ?, charger_price = ?, transport_price_per_km = ?
        WHERE email = ?
    ''', (company_name, company_DUNS, company_website, warehouse_address, price_per_panel, heatpump_price, battery_price, charger_price, transport_price_per_km, email_address))
    conn.commit()
    conn.close()


# Function to add a new admin
def register_admin(username, email, password):
    conn = get_db_connection('admins')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO admins (username, email, password)
        VALUES (?, ?, ?)
    ''', (username, email, password))
    conn.commit()
    conn.close()


def get_db_connection():
    conn = sqlite3.connect("database.db")
    return conn


# Function to check login
def check_login(email, password):
    tables = {
        'clients': 'clients',
        'providers': 'providers',
        'admins': 'admins'
    }

    # Query templates for each table
    queries = {
        'clients': "SELECT * FROM clients WHERE email = ? AND password = ?",
        'providers': "SELECT * FROM providers WHERE email_address = ? AND password = ?",
        'admins': "SELECT * FROM admins WHERE email = ? AND password = ?"
    }

    for table_name in tables.items():
        conn = get_db_connection()
        cursor = conn.cursor()

        # Execute the appropriate query
        cursor.execute(queries[table_name], (email, password))
        result = cursor.fetchone()

        if result:
            cursor.execute(f"UPDATE {table_name} SET active_user = TRUE WHERE email = ?", email)
            conn.commit()
            conn.close()
            return table_name, email  # Return the table name and user ID

    return None, None
