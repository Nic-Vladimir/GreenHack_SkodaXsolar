import sqlite3

# Function to create a database and a table
def create_database(db_name, table_name, table_schema):
    conn = sqlite3.connect(f'{db_name}.db')
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_schema})')
    conn.commit()
    conn.close()

# Schema definitions
clients_schema = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    fullname TEXT NOT NULL,
    password TEXT NOT NULL,
    user_address TEXT,
    current_energy REAL,
    panel_area REAL,
    vehicle TEXT,
    active_user BOOLEAN DEFAULT FALSE
'''

providers_schema = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    company_name TEXT NOT NULL,
    company_DUNS TEXT NOT NULL,
    company_website TEXT NOT NULL,
    warehouse_address TEXT,
    panel_price_per_meter REAL,
    heatpump_price REAL,
    battery_price REAL,
    charger_price REAL,
    transport_price_per_km REAL,
    active_user BOOLEAN DEFAULT FALSE,
    status TEXT DEFAULT Pending,
    reason_rejected TEXT NOT NULL
'''

admins_schema = '''
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    active_user BOOLEAN DEFAULT FALSE
'''

def databases_setup():
    # Create the databases and tables
    create_database('database', 'clients', clients_schema)
    create_database('database', 'providers', providers_schema)
    create_database('database', 'admins', admins_schema)

    print("Databases and tables setup complete.")
    

