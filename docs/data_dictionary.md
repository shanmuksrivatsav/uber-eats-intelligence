# Uber Eats Operational & Customer Intelligence System
## Data Dictionary

### 1. Customers — `customers.csv`

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| age | Customer age in years |
| city | Customer's registered city |
| membership | Membership category |
| signup_date | Date the customer joined |

### 2. Restaurants — `restaurants.csv`

| Column | Description |
|---|---|
| restaurant_id | Unique restaurant identifier |
| restaurant_name | Synthetic restaurant name |
| city | Restaurant's city |
| category | Type of cuisine or restaurant |
| restaurant_rating | Synthetic restaurant rating |
| avg_prep_time_minutes | Average food preparation time |

### 3. Drivers — `drivers.csv`

| Column | Description |
|---|---|
| driver_id | Unique driver identifier |
| vehicle_type | Driver's vehicle type |
| experience_months | Driving experience in months |
| driver_rating | Synthetic driver rating |

### 4. Orders — `orders.csv`

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer who placed the order |
| restaurant_id | Restaurant receiving the order |
| order_timestamp | Date and time of the order |
| order_amount | Order value before tip |
| number_of_items | Number of items ordered |
| delivery_distance_km | Delivery distance in kilometres |
| prep_time_minutes | Estimated preparation time |
| delivery_time_minutes | Synthetic delivery duration |
| traffic | Traffic condition |
| weather | Weather condition |
| is_weekend | 1 if Saturday or Sunday, otherwise 0 |
| peak_period_weight | Illustrative peak-hour multiplier |
| order_status | Delivered or Cancelled |

### 5. Deliveries — `deliveries.csv`

| Column | Description |
|---|---|
| delivery_id | Unique delivery identifier |
| order_id | Associated order |
| driver_id | Assigned driver |
| delivery_distance_km | Delivery distance in kilometres |
| delivery_time_minutes | Delivery duration |
| delivery_status | Delivery status |

### 6. Payments — `payments.csv`

| Column | Description |
|---|---|
| payment_id | Unique payment record identifier |
| order_id | Associated order |
| payment_method | Payment method |
| order_amount | Order value before tip |
| tip_amount | Synthetic tip amount |
| payment_status | Paid or Refunded |

### 7. Reviews — `reviews.csv`

| Column | Description |
|---|---|
| review_id | Unique review identifier |
| order_id | Associated order |
| customer_id | Customer submitting the review |
| restaurant_id | Reviewed restaurant |
| review_text | Synthetic customer feedback |
| sentiment_label | Synthetic Positive, Neutral or Negative label |
| review_rating | Synthetic rating from 1 to 5 |

## Data limitations

All records are synthetic and do not represent actual Uber Eats transactions. Review text and sentiment labels are generated from templates rather than genuine customer feedback. Delivery duration, tips, order status and payment status are simplified simulations and should be improved before drawing strong business conclusions.

Customer, restaurant, driver, order, delivery, review and payment identifiers establish relationships between datasets. Identifiers should not be used as numerical predictors in machine learning models.
