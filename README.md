# Uber Eats Operational & Customer Intelligence System

## Project Overview

The **Uber Eats Operational & Customer Intelligence System** is an end-to-end machine learning capstone project focused on food delivery and marketplace analytics.

The project uses synthetic data to analyze customer behavior, restaurant performance, customer feedback, delivery operations, and order demand. Machine learning models will be developed to identify actionable patterns and support data-driven business decisions.

## Project Objectives

- Segment customers and restaurants using K-Means and DBSCAN clustering.
- Analyze customer feedback using NLP and sentiment classification.
- Predict delivery time or tip amount using regression models.
- Forecast hourly order demand using ARIMA and Prophet.
- Integrate machine learning components into an end-to-end pipeline.
- Generate actionable business insights and recommendations.
- Maintain reproducible code, documentation, and version control using Git and GitHub.

## Technology Stack

- **Programming:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **NLP:** NLTK, TF-IDF, VADER
- **Time-Series Forecasting:** Statsmodels, Prophet
- **Visualization:** Matplotlib, Seaborn
- **Development Environment:** VS Code, Jupyter Notebook
- **Version Control:** Git and GitHub

## Project Structure

```text
uber-eats-intelligence/
│
├── data/
│   ├── synthetic/
│   └── processed/
│
├── src/
│   ├── data_generation.py
│   └── validate_data.py
│
├── docs/
│   ├── data_dictionary.md
│   └── prompt_engineering.md
│
├── notebooks/
├── models/
├── reports/
│   └── figures/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset Description

The project uses seven synthetic datasets:

| Dataset | Description |
|---|---|
| Customers | Customer demographics, city, membership, and signup date |
| Restaurants | Restaurant category, rating, city, and preparation time |
| Drivers | Driver vehicle type, experience, and rating |
| Orders | Order value, timestamp, distance, traffic, weather, and delivery duration |
| Deliveries | Delivery records linked to orders and drivers |
| Payments | Order payments, payment methods, tips, and payment status |
| Reviews | Synthetic customer feedback, ratings, and sentiment labels |

The datasets are connected through identifiers such as `customer_id`, `restaurant_id`, `driver_id`, and `order_id`.

**Note:** All records are synthetic and do not represent actual Uber Eats transactions.

## Project Roadmap

The capstone follows a seven-day schedule.

| Day | Focus Area |
|---|---|
| Day 1 | Project setup, Git workflow, synthetic data generation, and documentation |
| Day 2 | Data preparation, feature engineering, customer and restaurant segmentation |
| Day 3 | NLP preprocessing, sentiment analysis, and customer complaint identification |
| Day 4 | Delivery time or tip prediction using regression |
| Day 5 | Hourly order demand forecasting using ARIMA and Prophet |
| Day 6 | End-to-end ML pipeline and business insights |
| Day 7 | Final evaluation, documentation, Git finalization, and presentation |

## Setup and Execution

### 1. Clone the repository

```bash
git clone https://github.com/shanmuksrivatsav/uber-eats-intelligence.git
cd uber-eats-intelligence
```

### 2. Create and activate a virtual environment

On Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Generate synthetic datasets

```bash
python src/data_generation.py
```

### 5. Validate the datasets

```bash
python src/validate_data.py
```

Generated CSV files are stored in `data/synthetic/`.

## Expected Outcomes

By the end of the project, the system is expected to provide:

- Meaningful customer and restaurant segments.
- Customer sentiment classifications and major complaint themes.
- Evaluated regression models for delivery time or tip prediction.
- Hourly demand forecasts and comparisons between forecasting models.
- An integrated machine learning workflow.
- Business recommendations supported by analytical results.
- Documentation and a final presentation explaining the methodology, results, limitations, and potential improvements.

## Limitations

- Synthetic datasets cannot fully represent real-world food delivery behavior.
- Synthetic review text and sentiment labels may not generalize to actual customer feedback.
- Model performance depends on the quality, realism, and distribution of generated data.
- Business recommendations must be interpreted in the context of these limitations.

## Version Control

The project uses Git for version control and a feature branch for development.

Current development branch:

`feature/uber-eats-pipeline`

Meaningful commits will be maintained throughout the project to track data generation, preprocessing, model development, evaluation, and documentation.

## Disclaimer

This is an educational machine learning capstone project. It is not an official Uber Eats product and does not use proprietary Uber Eats data.
