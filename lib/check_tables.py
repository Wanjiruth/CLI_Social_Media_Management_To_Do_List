import sqlite3

# Connect to the database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Query to check for tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
conn.close()
