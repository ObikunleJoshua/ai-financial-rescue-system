import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Financial Rescue System", layout="wide")

# ---------------------------
# AUTO-SETUP DATABASE
# ---------------------------
import os

from src import (
    generate_financial_data,
    db_setup_financial,
    load_financial_data,
    transform_financial_data,
    train_model,
    generate_alerts
)

conn = sqlite3.connect("financial_monitoring.db")
cursor = conn.cursor()

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type='table' AND name='financial_metrics';
""")

table_exists = cursor.fetchone()

if not table_exists:
    db_setup_financial.main()
    generate_financial_data.main()
    load_financial_data.main()
    transform_financial_data.main()
    train_model.main()
    generate_alerts.main()

conn.close()

# ---------------------------
# LOAD DATA
# ---------------------------
conn = sqlite3.connect("financial_monitoring.db")

metrics_df = pd.read_sql("SELECT * FROM financial_metrics", conn)
alerts_df = pd.read_sql("SELECT * FROM alerts", conn)

conn.close()

metrics_df["date"] = pd.to_datetime(metrics_df["date"])

# ---------------------------
# HEADER
# ---------------------------
st.title("💰 AI Financial Rescue & Profit Optimization System")

st.markdown("""
This system predicts financial risks, identifies problem areas, and recommends actions to improve profitability.
""")

# ---------------------------
# KPI SECTION
# ---------------------------
total_profit = int(metrics_df["profit"].sum())
risk_count = int(metrics_df["predicted_risk"].sum())
regions_at_risk = metrics_df[metrics_df["predicted_risk"] == 1]["region"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Profit", f"{total_profit:,}")
col2.metric("⚠️ Risk Signals", risk_count)
col3.metric("🌍 Regions at Risk", regions_at_risk)

# ---------------------------
# ALERT PANEL
# ---------------------------
st.subheader("🚨 Critical Alerts")

if len(alerts_df) > 0:
    st.dataframe(alerts_df.sort_values(by="date", ascending=False).head(10))
else:
    st.success("No major risks detected.")

# ---------------------------
# TREND CHART
# ---------------------------
st.subheader("📈 Profit Trend Over Time")

trend = metrics_df.groupby("date")["profit"].sum().reset_index()

fig = px.line(
    trend,
    x="date",
    y="profit",
    title="Total Profit Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------
# RISK DISTRIBUTION
# ---------------------------
st.subheader("⚠️ Risk Distribution")

risk_dist = metrics_df["predicted_risk"].value_counts().reset_index()
risk_dist.columns = ["risk_flag", "count"]

fig2 = px.bar(
    risk_dist,
    x="risk_flag",
    y="count",
    title="Risk vs Safe Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# REGION FILTER
# ---------------------------
st.sidebar.header("Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    options=metrics_df["region"].unique(),
    default=metrics_df["region"].unique()
)

filtered_df = metrics_df[metrics_df["region"].isin(regions)]

# ---------------------------
# REGION PERFORMANCE
# ---------------------------
st.subheader("📊 Regional Performance")

region_perf = filtered_df.groupby("region")[["profit"]].sum().reset_index()

fig3 = px.bar(
    region_perf,
    x="region",
    y="profit",
    title="Profit by Region"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# RECOMMENDATIONS
# ---------------------------
st.subheader("💡 Recommended Actions")

if len(alerts_df) > 0:
    st.dataframe(alerts_df[["region", "alert_message", "recommendation"]].drop_duplicates().head(10))
else:
    st.info("No recommendations needed.")