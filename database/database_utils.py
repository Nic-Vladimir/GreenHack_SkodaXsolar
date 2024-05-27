import sqlite3

# Function to connect to a database
def get_db_connection(db_name):
    conn = sqlite3.connect(f'{db_name}.db')
    return conn


# User registration
def register_client(fullname, username, client_email, password):
    conn = get_db_connection('clients')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clients (fullname, username, client_email, password)
        VALUES (?, ?, ?, ?)
    ''', (fullname, username, client_email, password))
    conn.commit()
    conn.close()


# Function to update client info
def add_client_info(client_email, user_address, current_energy, panel_area, vehicle):
    conn = get_db_connection('clients')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clients
        SET user_address = ?, current_energy = ?, panel_area = ?, vehicle = ?
        WHERE client_email = ?
    ''', (user_address, current_energy, panel_area, vehicle, client_email))
    conn.commit()
    conn.close()


# Function to add a new provider
def add_provider(company_name, email_address, warehouse_address, panel_price_per_meter, heatpump_price, battery_price, charger_price, transport_price_per_km):
    conn = get_db_connection('providers')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO providers (company_name, email_address, warehouse_address, panel_price_per_meter, heatpump_price, battery_price, charger_price, transport_price_per_km)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (company_name, email_address, warehouse_address, panel_price_per_meter, heatpump_price, battery_price, charger_price, transport_price_per_km))
    conn.commit()
    conn.close()


# Function to add a new admin
def add_admin(username, password):
    conn = get_db_connection('admins')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO admins (username, password)
        VALUES (?, ?)
    ''', (username, password))
    conn.commit()
    conn.close()
