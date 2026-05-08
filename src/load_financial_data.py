import pandas as pd
import sqlite3

def main():
    df = pd.read_csv("data/financial_data.csv")

    conn = sqlite3.connect("financial_monitoring.db")

    conn.execute("DELETE FROM raw_financial_data")

    df.to_sql("raw_financial_data", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    print("Raw financial data loaded.")

if __name__ == "__main__":
    main()