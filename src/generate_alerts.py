import pandas as pd
import sqlite3

def main():
    conn = sqlite3.connect("financial_monitoring.db")

    df = pd.read_sql("SELECT * FROM financial_metrics", conn)
    clean_df = pd.read_sql("SELECT * FROM clean_financial_data", conn)

    conn.close()

    # Merge to get more features
    df = df.merge(
        clean_df,
        on=["date", "region", "profit", "revenue", "cost"],
        how="left"
    )

    alerts = []

    for _, row in df.iterrows():

        if row["predicted_risk"] == 1:

            message = ""
            recommendation = ""

            # ---------------------------
            # DIAGNOSIS LOGIC
            # ---------------------------

            if row["cost"] > row["revenue"] * 0.8:
                message = "High operational cost detected"
                recommendation = "Consider reducing operational expenses"

            elif row["revenue"] < row["avg_revenue_7d"]:
                message = "Revenue declining below trend"
                recommendation = "Improve sales strategy or pricing"

            elif row["marketing_efficiency"] < 2:
                message = "Marketing inefficiency detected"
                recommendation = "Optimize marketing campaigns"

            elif row["orders"] < row["avg_revenue_7d"] * 0.02:
                message = "Low order volume"
                recommendation = "Improve conversion funnel"

            else:
                message = "General performance risk"
                recommendation = "Review business operations"

            alerts.append([
                row["date"],
                row["region"],
                message,
                recommendation
            ])

    alerts_df = pd.DataFrame(alerts, columns=[
        "date",
        "region",
        "alert_message",
        "recommendation"
    ])

    # Save alerts
    conn = sqlite3.connect("financial_monitoring.db")

    alerts_df.to_sql("alerts", conn, if_exists="replace", index=False)

    conn.close()

    print("Alerts and recommendations generated.")

if __name__ == "__main__":
    main()