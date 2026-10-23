# Prompt Engineering — Synthetic Uber Eats Data

## Objective

Generate reproducible synthetic datasets for an end-to-end food delivery analytics project.

## 1. P.T.C.F. Prompt

**Persona:** Act as a senior data engineer and machine learning practitioner specializing in food-delivery analytics.

**Task:** Develop a Python script that generates seven connected synthetic datasets: customers, restaurants, drivers, orders, deliveries, reviews and payments.

**Context:** The datasets will be used to demonstrate customer and restaurant segmentation, sentiment analysis, delivery-time or tip prediction, and hourly demand forecasting. Use realistic relationships between order characteristics, traffic, weather, preparation time, delivery duration and customer feedback. Maintain primary keys, foreign keys and consistent record relationships.

**Format:** Return executable Python code using Pandas and NumPy. Save each dataset as a separate CSV file in `data/synthetic/`. Use reproducible random generation, clear comments and a summary of row counts. Document assumptions and limitations.

## 2. Few-Shot Prompting

Examples of expected synthetic relationships:

- Example 1: A longer delivery distance should generally increase delivery time, other factors being equal.
- Example 2: High traffic should generally increase delivery time compared with low traffic.
- Example 3: A review stating that delivery was late and food was cold should receive a negative sentiment label.
- Example 4: A completed order should have a corresponding delivery record.

These examples communicate the expected behavior to the model; they are not evidence that the generated data reflects actual marketplace behavior.

## 3. Structured Output Prompt

Generate the datasets with these requirements:

- Seven separate CSV files.
- Unique primary keys.
- Valid foreign-key relationships.
- Numeric values for continuous variables.
- Consistent timestamps.
- Documented categorical values.
- Reproducible random seed.
- Data dictionary and validation checks.
- Explicit identification of synthetic assumptions.

## 4. Limitations and Validation

Review the generated script for logical consistency, missing values, duplicate identifiers, invalid foreign keys, unrealistic distributions and assumptions that could bias downstream model evaluation.

## 5. Reproducibility

Record the generation script version, random seed, dataset sizes, Python dependencies and Git commit so the datasets can be regenerated.
