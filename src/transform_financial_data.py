import pandas as pd
import sqlite3

def main():
    conn = sqlite3.connect("financial_monitoring.db")

    df = pd.read_sql("SELECT * FROM raw_financial_data", conn)

    # Convert date
    df["date"] = pd.to_datetime(df["date"])

    # Sort for rolling calculations
    df = df.sort_values(by=["region", "date"])

    # ---------------------------
    # CORE METRICS
    # ---------------------------
    df["profit"] = df["revenue"] - df["cost"]

    df["conversion_rate"] = df["orders"] / (df["customers"] + 1)

    df["cost_per_order"] = df["cost"] / (df["orders"] + 1)

    df["marketing_efficiency"] = df["revenue"] / (df["marketing_spend"] + 1)

    # ---------------------------
    # TREND FEATURES (IMPORTANT)
    # ---------------------------
    df["avg_profit_7d"] = df.groupby("region")["profit"].transform(
        lambda x: x.rolling(window=7, min_periods=1).mean()
    )

    df["avg_revenue_7d"] = df.groupby("region")["revenue"].transform(
        lambda x: x.rolling(window=7, min_periods=1).mean()
    )

    # ---------------------------
    # SAVE CLEAN DATA
    # ---------------------------
    df.to_sql("clean_financial_data", conn, if_exists="replace", index=False)

    conn.close()

    print("Financial data transformed (Silver layer complete).")


if __name__ == "__main__":
    main()