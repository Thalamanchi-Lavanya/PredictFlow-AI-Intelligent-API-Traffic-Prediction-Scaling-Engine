import sqlite3
import pandas as pd

# Create Database Connection
conn = sqlite3.connect("traffic.db")

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requests INTEGER,
    cpu INTEGER,
    memory INTEGER
)
""")

# Read CSV
df = pd.read_csv("traffic_logs.csv")

# Insert Data
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO traffic_logs
        (requests, cpu, memory)
        VALUES (?, ?, ?)
        """,
        (
            int(row["requests"]),
            int(row["cpu"]),
            int(row["memory"])
        )
    )

conn.commit()
conn.close()

print("CSV Data Inserted Successfully")