import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="your_password",  # <-- change this
    port="5432"
)

cur = conn.cursor()

# Take input
name = input("Enter name: ")
email = input("Enter email: ")

# Insert data
cur.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    (name, email)
)
conn.commit()

print("\n✅ Data inserted successfully!\n")

# Fetch data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("📄 Stored Records:")
for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
