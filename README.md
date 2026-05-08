# AI Financial Rescue & Profit Optimization System

An AI-driven financial monitoring system designed to detect profit risks, identify operational inefficiencies, and recommend corrective business actions using machine learning and KPI analysis.

---

## Dashboard Preview

![Dashboard](images/dashboard.png)
![Dashboard](images/recommended_actions.png)
![Dashboard](images/profit-trends.png)
![Dashboard](images/regional_performance.png)

---

## Project Overview

This system simulates a real-world business environment where financial performance is monitored across multiple regions.

The platform:
- Tracks operational KPIs
- Detects potential profit decline
- Predicts financial risk using machine learning
- Generates alerts and business recommendations
- Visualizes insights through an interactive dashboard

---

## Key Features

### KPI Monitoring
Tracks critical business metrics such as:
- Revenue
- Cost
- Profit
- Orders
- Marketing Spend
- Conversion Rate

---

### Machine Learning Risk Prediction
Uses a Random Forest classification model to predict:
- Future profit decline
- High-risk business regions

---

### Intelligent Alert System
Automatically detects:
- Revenue decline
- Cost spikes
- Low operational efficiency
- Marketing inefficiency

---

### Recommendation Engine
Provides actionable business suggestions such as:
- Reduce operational costs
- Improve sales strategy
- Optimize marketing campaigns
- Improve conversion performance

---

### Interactive Dashboard
Built with Streamlit and Plotly for:
- KPI visualization
- Trend analysis
- Risk monitoring
- Regional performance comparison

---

## System Architecture

```text
Raw Financial Data (CSV)
        ↓
SQL Database (SQLite)
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Risk Prediction
        ↓
Alert & Recommendation Engine
        ↓
Interactive Dashboard
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming |
| Pandas | Data processing |
| SQLite | Database storage |
| Scikit-learn | Machine learning |
| Streamlit | Dashboard interface |
| Plotly | Interactive charts |

---

## Project Structure

```text
ai-financial-rescue-system/
│── app.py
│── requirements.txt
│── README.md
│
├── data/
│   └── financial_data.csv
│
├── images/
│   └── dashboard.png
│
├── src/
│   ├── generate_financial_data.py
│   ├── db_setup_financial.py
│   ├── load_financial_data.py
│   ├── transform_financial_data.py
│   ├── train_model.py
│   └── generate_alerts.py
```

---

## How the System Works

### Data Generation
Synthetic financial data is generated to simulate:
- Revenue trends
- Cost fluctuations
- Demand drops
- Marketing inefficiencies

---

### Data Storage
Raw data is loaded into a structured SQL database.

---

### Feature Engineering
Business metrics are calculated, including:
- Profit
- Conversion Rate
- Marketing Efficiency
- Rolling Revenue Trends

---

### Machine Learning
A Random Forest model predicts whether a region is at financial risk based on historical behavior.

---

### Alert Generation
The system analyzes predictions and generates business alerts and recommendations.

---

### Visualization
All insights are displayed through an interactive dashboard.

---

## Example Business Questions Answered

- Which regions are likely to experience profit decline?
- Are operational costs becoming unsustainable?
- Is marketing spend producing sufficient returns?
- Which business areas require immediate attention?

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run data pipeline

```bash
python src/db_setup_financial.py
python src/generate_financial_data.py
python src/load_financial_data.py
python src/transform_financial_data.py
python src/train_model.py
python src/generate_alerts.py
```

---

### Launch dashboard

```bash
python -m streamlit run app.py
```

---

## Machine Learning Approach

### Model Used
- Random Forest Classifier

### Prediction Goal
Predict whether a business region is at risk of significant future profit decline.

### Features Used
- Revenue
- Cost
- Orders
- Customers
- Marketing Spend
- Profit Trends
- Conversion Metrics

---

## Business Value

This system demonstrates how data and machine learning can be used to:
- Improve operational visibility
- Detect financial risks early
- Support strategic business decisions
- Optimize profitability

---

## Future Improvements

- Real-time API ingestion
- Cloud database integration
- Airflow orchestration
- Email/SMS alerting
- Advanced forecasting models

---

## 👤 Author

**Joshua OBIKUNLE**