import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def main():
    conn = sqlite3.connect("financial_monitoring.db")

    df = pd.read_sql("SELECT * FROM clean_financial_data", conn)

    conn.close()

    # ---------------------------
    # CREATE TARGET (future profit)
    # ---------------------------
    df = df.sort_values(by=["region", "date"])

    df["future_profit"] = df.groupby("region")["profit"].shift(-7)

    # Define risk: profit drop > 20%
    df["risk_flag"] = (
        (df["future_profit"] < df["profit"] * 0.8)
    ).astype(int)

    # Drop null rows (from shifting)
    df = df.dropna()

    # ---------------------------
    # FEATURES
    # ---------------------------
    features = [
        "revenue",
        "cost",
        "orders",
        "customers",
        "marketing_spend",
        "profit",
        "conversion_rate",
        "cost_per_order",
        "marketing_efficiency",
        "avg_profit_7d",
        "avg_revenue_7d"
    ]

    X = df[features]
    y = df["risk_flag"]

    # ---------------------------
    # TRAIN / TEST SPLIT
    # ---------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------------------------
    # MODEL
    # ---------------------------
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nMODEL PERFORMANCE:\n")
    print(classification_report(y_test, predictions))

    # ---------------------------
    # SAVE RESULTS
    # ---------------------------
    df["predicted_risk"] = model.predict(X)

    conn = sqlite3.connect("financial_monitoring.db")

    df[[
        "date",
        "region",
        "profit",
        "revenue",
        "cost",
        "risk_flag",
        "predicted_risk"
    ]].to_sql("financial_metrics", conn, if_exists="replace", index=False)

    conn.close()

    print("Model training complete and results saved.")

if __name__ == "__main__":
    main()