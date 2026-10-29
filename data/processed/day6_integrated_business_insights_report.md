# Day 6 – Integrated ML Pipeline and Business Insights

## Objective
Integrate the outputs of customer/restaurant segmentation, sentiment analysis, delivery-time regression, and demand forecasting into a concise business-facing summary.

## Data inventory
| table       |   rows |   columns |   duplicate_rows |   missing_cells |
|:------------|-------:|----------:|-----------------:|----------------:|
| orders      |  10000 |        14 |                0 |               0 |
| deliveries  |   9358 |         6 |                0 |               0 |
| customers   |   1000 |         5 |                0 |               0 |
| restaurants |    100 |         6 |                0 |               0 |
| drivers     |    200 |         4 |                0 |               0 |
| payments    |  10000 |         6 |                0 |               0 |
| reviews     |   7000 |         7 |                0 |               0 |

## KPI summary
| kpi                        | value            | source                    | interpretation                                         |
|:---------------------------|:-----------------|:--------------------------|:-------------------------------------------------------|
| Total orders               | 10000            | orders.csv                | Number of order records in the synthetic dataset.      |
| Total customers            | 1000             | customers.csv             | Number of customer records in the synthetic dataset.   |
| Total restaurants          | 100              | restaurants.csv           | Number of restaurant records in the synthetic dataset. |
| Delivery status categories | 1                | deliveries.csv            | Status field used: delivery_status.                    |
| Best delivery-time model   | Lasso Regression | Day 4 model comparison    | MAE=4.025 minutes; RMSE=5.033; R²=0.909.               |
| Best demand forecast model | ARIMA(1, 0, 1)   | Day 5 forecast comparison | Lowest test MAE=1.205 orders/hour.                     |

## Evidence-based insights and recommendations
| area                     | evidence                                                                                  | business_implication                                                                             | recommendation                                                                                                                                          | limitation                                          |
|:-------------------------|:------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------|
| Customer segmentation    | Customer cluster profiles are available with 2 cluster rows.                              | Customer groups may differ in order frequency, value, or engagement.                             | Use the profile columns to design differentiated retention or loyalty experiments; prioritize groups using the actual metrics in the profile table.     | Synthetic dataset; validate before operational use. |
| Restaurant segmentation  | Restaurant cluster profiles are available with 2 cluster rows.                            | Restaurant groups may differ in volume, ratings, preparation time, or cancellations.             | Review high-preparation-time or high-cancellation profiles and investigate operational support using the measured profile values.                       | Synthetic dataset; validate before operational use. |
| Customer sentiment       | 2373 negative-labeled reviews out of 7000 (33.9%) based on the detected sentiment column. | Negative feedback may highlight recurring service pain points.                                   | Inspect the top negative-review themes and validate them against delivery and restaurant operational metrics.                                           | Synthetic dataset; validate before operational use. |
| Delivery-time prediction | Lasso Regression had the lowest saved test MAE (4.02 minutes).                            | The model's error indicates how closely estimates matched held-out synthetic delivery durations. | Use the model as a prototype for estimated-delivery-time support only after checking feature availability at prediction time and testing on fresh data. | Synthetic dataset; validate before operational use. |
| Demand planning          | Highest average demand hour from saved hourly series: 1:00.                               | Recurring peak hours can help align staffing and delivery capacity with expected demand.         | Use the next-24-hour forecast and weekday/weekend pattern to plan a small capacity pilot; compare predicted demand with actuals after the period.       | Synthetic dataset; validate before operational use. |

## Model evaluation references
### Day 4 regression model comparison
| Model             |      MAE |     RMSE |         R2 |
|:------------------|---------:|---------:|-----------:|
| Lasso Regression  |  4.02452 |  5.03251 |  0.90901   |
| Ridge Regression  |  4.19661 |  5.24339 |  0.901224  |
| Random Forest     |  4.3804  |  5.50645 |  0.891064  |
| Linear Regression |  4.52397 |  5.63414 |  0.885953  |
| Dummy Baseline    | 13.2046  | 16.7738  | -0.0108622 |

### Day 5 forecast model comparison
| Model                   |     MAE |    RMSE |   MAPE_percent_nonzero_actuals |
|:------------------------|--------:|--------:|-------------------------------:|
| ARIMA(1, 0, 1)          | 1.20473 | 1.51144 |                        56.8263 |
| Seasonal Naive Baseline | 1.49074 | 1.94841 |                        73.2205 |

## Limitations
- All data is synthetic; conclusions are illustrative, not real-world claims.
- This notebook integrates saved artifacts and does not retrain all previous models from scratch.
- Results depend on the quality and availability of Day 2–Day 5 outputs.
- Predictive feature importance does not prove causation.
- Features used for a live prediction must be available at the time that prediction is made.
- Recommendations should be validated with real operational data and controlled experiments.

## Suggested next steps
1. Confirm all Day 2–Day 5 outputs are generated and consistent.
2. Review the highest-impact customer complaints alongside delivery metrics.
3. Validate delivery-time model performance on a later time period.
4. Compare demand forecasts with actual orders and refine staffing assumptions.
5. Prepare Day 7 presentation with measured results and limitations.