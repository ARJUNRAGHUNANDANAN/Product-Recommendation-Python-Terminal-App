import sqlite3, pandas as pd

df = pd.read_csv('raw_data/laptops.csv', encoding='ISO-8859-1')
df.columns = df.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df = df.dropna()

conn = sqlite3.connect('/inventory_normalized/normalized_inventory.sqlite')
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS laptops")
cursor.execute("DROP TABLE IF EXISTS manufacturers")
cursor.execute("DROP TABLE IF EXISTS operating_systems")
cursor.execute("DROP TABLE IF EXISTS categories")

# Create tables
cursor.execute('''CREATE TABLE manufacturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)''')
cursor.execute('''CREATE TABLE operating_systems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    version TEXT NOT NULL,
    UNIQUE(name, version)
)''')
cursor.execute('''CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)''')
cursor.execute('''CREATE TABLE laptops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER,
    model_name TEXT NOT NULL,
    category_id INTEGER,
    screen_size TEXT,
    screen TEXT,
    cpu TEXT,
    ram TEXT,
    storage TEXT,
    gpu TEXT,
    operating_system_id INTEGER,
    weight TEXT,
    price_euros REAL,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id),
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (operating_system_id) REFERENCES operating_systems(id)
)''')

# Populate  tables
manufacturers = pd.DataFrame(df['Manufacturer'].unique(), columns=['name'])
manufacturers.to_sql('manufacturers', conn, if_exists='append', index=False)
operating_systems = df[['Operating_System', 'Operating_System_Version']].drop_duplicates().rename(
    columns={'Operating_System': 'name', 'Operating_System_Version': 'version'})
operating_systems.to_sql('operating_systems', conn, if_exists='append', index=False)
categories = pd.DataFrame(df['Category'].unique(), columns=['name'])
categories.to_sql('categories', conn, if_exists='append', index=False)
for _, row in df.iterrows():
    manufacturer_id = cursor.execute("SELECT id FROM manufacturers WHERE name = ?", (row['Manufacturer'],)).fetchone()[0]
    category_id = cursor.execute("SELECT id FROM categories WHERE name = ?", (row['Category'],)).fetchone()[0]
    os_id = cursor.execute("SELECT id FROM operating_systems WHERE name = ? AND version = ?",
                           (row['Operating_System'], row['Operating_System_Version'])).fetchone()[0]

    cursor.execute('''INSERT INTO laptops (manufacturer_id, model_name, category_id, screen_size, screen, cpu, ram, storage, gpu, operating_system_id, weight, price_euros)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (manufacturer_id, row['Model_Name'], category_id, row['Screen_Size'], row['Screen'], row['CPU'], row['RAM'], row['_Storage'], row['GPU'], os_id, row['Weight'], row['Price_Euros']))

conn.commit()
conn.close()
print("Done")