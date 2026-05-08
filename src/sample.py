import sqlite3
import pandas as pd

conn = sqlite3.connect("financial_monitoring.db")

df = pd.read_sql("SELECT * FROM alerts LIMIT 10", conn)
print(df)

conn.close()