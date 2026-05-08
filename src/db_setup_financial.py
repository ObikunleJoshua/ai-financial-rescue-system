import sqlite3

def main():
    conn = sqlite3.connect("financial_monitoring.db")
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS raw_financial_data (
        date DATE,
        region TEXT,
        revenue REAL,
        cost REAL,
        orders INTEGER,
        customers INTEGER,
        marketing_spend REAL
    );

    CREATE TABLE IF NOT EXISTS clean_financial_data (
        date DATE,
        region TEXT,
        revenue REAL,
        cost REAL,
        orders INTEGER,
        customers INTEGER,
        marketing_spend REAL,
        profit REAL,
        conversion_rate REAL,
        cost_per_order REAL,
        marketing_efficiency REAL
    );

    CREATE TABLE IF NOT EXISTS financial_metrics (
        date DATE,
        region TEXT,
        profit REAL,
        revenue REAL,
        cost REAL,
        risk_flag INTEGER
    );
    """)

    conn.commit()
    conn.close()

    print("Financial DB setup complete.")

if __name__ == "__main__":
    main()