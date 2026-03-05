import sqlite3
from transform import transform

df = transform()

# Connect to a SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("medicare.db")

# Save the DataFrame as a table called "medicare_claims"
df.to_sql("medicare_claims", conn, if_exists="replace", index=False)

conn.close()

print(f"Loaded {len(df)} rows into medicare.db")