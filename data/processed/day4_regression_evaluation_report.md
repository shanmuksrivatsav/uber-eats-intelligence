# Day 4 – Delivery Time Prediction: Evaluation Report

## Dataset and target
- Modeling rows after target cleaning: 9358
- Target column: `delivery_time_minutes`
- Number of model features: 29
- Training rows: 7486
- Test rows: 1872

## Test-set model comparison
| Model             |     MAE |    RMSE |      R2 |
|:------------------|--------:|--------:|--------:|
| Lasso Regression  |  4.0245 |  5.0325 |  0.9090 |
| Ridge Regression  |  4.1966 |  5.2434 |  0.9012 |
| Random Forest     |  4.3804 |  5.5065 |  0.8911 |
| Linear Regression |  4.5240 |  5.6341 |  0.8860 |
| Dummy Baseline    | 13.2046 | 16.7738 | -0.0109 |

## Cross-validation
| Model             |   CV_MAE_mean |   CV_MAE_std |   CV_RMSE_mean |   CV_RMSE_std |   CV_R2_mean |   CV_R2_std |
|:------------------|--------------:|-------------:|---------------:|--------------:|-------------:|------------:|
| Lasso Regression  |        4.0112 |       0.0955 |         5.0328 |        0.1122 |       0.9071 |      0.0046 |
| Ridge Regression  |        4.1696 |       0.0939 |         5.2379 |        0.1045 |       0.8994 |      0.0044 |
| Linear Regression |        4.3670 |       0.1135 |         5.4926 |        0.1134 |       0.8894 |      0.0050 |
| Random Forest     |        4.3958 |       0.0745 |         5.5438 |        0.1195 |       0.8873 |      0.0054 |
| Dummy Baseline    |       13.0465 |       0.1939 |        16.5996 |        0.2704 |      -0.0092 |      0.0051 |

## Recommended model
- Best model by held-out test MAE: **Lasso Regression**
- MAE: 4.025 minutes
- RMSE: 5.033 minutes
- R²: 0.909
- Cross-validation mean MAE: 4.011 ± 0.095 minutes

## Business interpretation
The selected model's average absolute error is approximately 4.0 minutes on the held-out test set. Use this error magnitude to judge whether the model could support delivery-time estimates. Review the permutation-importance table to identify features that appear most useful, and validate whether those features are available at the time a prediction would actually be made.

## Limitations
- The data is synthetic and may not represent real delivery behavior.
- Some potential predictors may be missing or represented by simplified fields.
- If a feature is only known after delivery, it must not be used for live predictions.
- Random train/test split assumes rows are sufficiently independent; future production validation may need a time-based split.
- Feature importance describes predictive association, not causation.

## Generated outputs
- `day4_regression_model_comparison.csv`
- `day4_cross_validation_results.csv`
- `day4_test_predictions.csv`
- `day4_permutation_importance.csv`
- `day4_feature_engineered_dataset.csv`
- Figures in `reports/figures/` prefixed with `day4_`