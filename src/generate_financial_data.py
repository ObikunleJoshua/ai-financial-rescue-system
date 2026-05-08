import pandas as pd
import numpy as np
import os

def main():
    os.makedirs("data", exist_ok=True)

    np.random.seed(42)

    dates = pd.date_range(start="2024-01-01", end="2024-06-30")
    regions = ["North", "South", "East", "West"]

    data = []

    for date in dates:
        for region in regions:

            base_revenue = np.random.randint(2000, 5000)
            base_orders = np.random.randint(80, 200)
            base_customers = base_orders + np.random.randint(10, 50)
            base_cost = base_revenue * np.random.uniform(0.5, 0.8)
            marketing_spend = np.random.randint(200, 1000)

            data.append([
                date,
                region,
                base_revenue,
                base_cost,
                base_orders,
                base_customers,
                marketing_spend
            ])

    df = pd.DataFrame(data, columns=[
        "date", "region", "revenue", "cost", "orders", "customers", "marketing_spend"
    ])

    # ---------------------------
    # Inject realistic problems
    # ---------------------------

    # Cost explosion
    df.loc[200:220, "cost"] *= 1.8

    # Demand drop
    df.loc[300:320, "revenue"] *= 0.6
    df.loc[300:320, "orders"] *= 0.6

    # Marketing inefficiency
    df.loc[400:420, "marketing_spend"] *= 2

    df.to_csv("data/financial_data.csv", index=False)

    print("Financial data generated.")

if __name__ == "__main__":
    main()