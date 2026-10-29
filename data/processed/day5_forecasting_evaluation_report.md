# Day 5 – Hourly Demand Forecasting Report

## Data preparation
- Source: `data/synthetic/orders.csv`
- Timestamp column: `order_timestamp`
- Hourly observations: 4319
- Time range: 2026-01-01 01:00:00 to 2026-06-29 23:00:00
- Mean hourly demand: 2.315 orders

## Exploratory findings
- Highest average-demand hour: 1:00
- Average orders during that hour: 2.561

## ADF results
| series                          |   adf_statistic |   p_value |   used_lags |   observations |   critical_1_percent |   critical_5_percent |   critical_10_percent |
|:--------------------------------|----------------:|----------:|------------:|---------------:|---------------------:|---------------------:|----------------------:|
| Original hourly demand          |        -35.0147 |    0.0000 |           3 |           4315 |              -3.4319 |              -2.8622 |               -2.5671 |
| First-differenced hourly demand |        -19.9802 |    0.0000 |          31 |           4286 |              -3.4319 |              -2.8622 |               -2.5671 |

## Forecast comparison
| Model                   |    MAE |   RMSE |   MAPE_percent_nonzero_actuals |
|:------------------------|-------:|-------:|-------------------------------:|
| ARIMA(1, 0, 1)          | 1.2047 | 1.5114 |                        56.8263 |
| Seasonal Naive Baseline | 1.4907 | 1.9484 |                        73.2205 |

## Selected model
- Lowest test MAE: **ARIMA(1, 0, 1)**
- MAE: 1.205 orders/hour
- RMSE: 1.511 orders/hour
- MAPE (nonzero actual hours): 56.826%
- Prophet status: Skipped: Prophet is not installed

## Business interpretation
In this synthetic dataset, average demand is highest around 1:00. Forecasts may help plan staffing and delivery capacity around expected peaks. Validate patterns and metrics before making operational recommendations.

## Limitations
- Synthetic data may not represent real demand.
- The date range may be too short for yearly seasonality or holiday effects.
- MAPE excludes hours with zero actual demand.
- Evaluation uses one chronological holdout; rolling-origin validation could provide stronger evidence.
- Forecast association does not establish causes.

## Outputs
- `day5_hourly_demand.csv`
- `day5_adf_test_results.csv`
- `day5_forecast_model_comparison.csv`
- `day5_test_forecasts.csv`
- `day5_next_24_hour_forecast.csv`
- Figures with prefix `day5_` in `reports/figures/`