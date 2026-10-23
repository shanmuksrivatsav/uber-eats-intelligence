import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
rng = np.random.default_rng(42)

OUTPUT_DIR = Path("data/synthetic")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 1. CUSTOMERS
# --------------------------------------------------
n_customers = 1000

customers = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, n_customers + 1)],
    "age": rng.integers(18, 66, n_customers),
    "city": rng.choice(
        ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi"],
        n_customers
    ),
    "membership": rng.choice(
        ["Regular", "Gold", "Premium"],
        n_customers,
        p=[0.60, 0.28, 0.12]
    ),
    "signup_date": pd.to_datetime(
        rng.integers(
            pd.Timestamp("2024-01-01").value // 10**9,
            pd.Timestamp("2026-01-01").value // 10**9,
            n_customers
        ),
        unit="s"
    ).date
})

# --------------------------------------------------
# 2. RESTAURANTS
# --------------------------------------------------
n_restaurants = 100

restaurants = pd.DataFrame({
    "restaurant_id": [f"R{i:03d}" for i in range(1, n_restaurants + 1)],
    "restaurant_name": [
        f"Restaurant_{i:03d}" for i in range(1, n_restaurants + 1)
    ],
    "city": rng.choice(
        ["Hyderabad", "Bengaluru", "Chennai", "Mumbai", "Delhi"],
        n_restaurants
    ),
    "category": rng.choice(
        ["Indian", "Chinese", "Italian", "Fast Food", "Healthy", "Desserts"],
        n_restaurants
    ),
    "restaurant_rating": np.round(
        rng.uniform(3.0, 5.0, n_restaurants), 1
    ),
    "avg_prep_time_minutes": rng.integers(10, 41, n_restaurants)
})

# --------------------------------------------------
# 3. DRIVERS
# --------------------------------------------------
n_drivers = 200

drivers = pd.DataFrame({
    "driver_id": [f"D{i:03d}" for i in range(1, n_drivers + 1)],
    "vehicle_type": rng.choice(
        ["Bike", "Scooter", "Car"],
        n_drivers,
        p=[0.25, 0.60, 0.15]
    ),
    "experience_months": rng.integers(1, 73, n_drivers),
    "driver_rating": np.round(
        rng.uniform(3.5, 5.0, n_drivers), 1
    )
})

# --------------------------------------------------
# 4. ORDERS
# --------------------------------------------------
n_orders = 10000

order_timestamps = (
    pd.Timestamp("2026-01-01")
    + pd.to_timedelta(
        rng.integers(0, 180 * 24 * 60, n_orders), unit="m"
    )
)

order_hours = order_timestamps.hour
is_weekend = order_timestamps.dayofweek >= 5

# More orders during lunch and dinner
peak_multiplier = np.where(
    ((order_hours >= 12) & (order_hours <= 14))
    | ((order_hours >= 18) & (order_hours <= 21)),
    1.20,
    1.0
)

# Synthetic records are sampled across the period.
# The multiplier is retained as a demand-related feature.
base_amount = rng.gamma(shape=3.0, scale=180.0, size=n_orders)
number_of_items = rng.integers(1, 9, n_orders)
order_amount = np.round(base_amount + number_of_items * 20, 2)

restaurant_indices = rng.integers(0, n_restaurants, n_orders)
customer_indices = rng.integers(0, n_customers, n_orders)

restaurant_prep = restaurants["avg_prep_time_minutes"].to_numpy()[
    restaurant_indices
]

distance_km = np.round(rng.gamma(2.0, 2.0, n_orders) + 0.3, 2)
traffic = rng.choice(
    ["Low", "Medium", "High"], n_orders, p=[0.30, 0.45, 0.25]
)
weather = rng.choice(
    ["Clear", "Rainy", "Cloudy"], n_orders, p=[0.55, 0.20, 0.25]
)

traffic_delay = pd.Series(traffic).map(
    {"Low": 0, "Medium": 6, "High": 15}
).to_numpy()

weather_delay = pd.Series(weather).map(
    {"Clear": 0, "Cloudy": 3, "Rainy": 10}
).to_numpy()

delivery_time = np.maximum(
    10,
    restaurant_prep
    + distance_km * 4
    + traffic_delay
    + weather_delay
    + rng.normal(0, 5, n_orders)
).round().astype(int)

order_status = rng.choice(
    ["Delivered", "Cancelled"],
    n_orders,
    p=[0.94, 0.06]
)

orders = pd.DataFrame({
    "order_id": [f"O{i:05d}" for i in range(1, n_orders + 1)],
    "customer_id": customers["customer_id"].to_numpy()[customer_indices],
    "restaurant_id": restaurants["restaurant_id"].to_numpy()[restaurant_indices],
    "order_timestamp": order_timestamps,
    "order_amount": order_amount,
    "number_of_items": number_of_items,
    "delivery_distance_km": distance_km,
    "prep_time_minutes": restaurant_prep,
    "delivery_time_minutes": delivery_time,
    "traffic": traffic,
    "weather": weather,
    "is_weekend": is_weekend.astype(int),
    "peak_period_weight": peak_multiplier,
    "order_status": order_status
})

# --------------------------------------------------
# 5. DELIVERIES
# Only completed orders receive a delivery record.
# --------------------------------------------------
delivered_orders = orders.loc[
    orders["order_status"] == "Delivered"
].copy()

delivery_driver_indices = rng.integers(
    0, n_drivers, len(delivered_orders)
)

deliveries = pd.DataFrame({
    "delivery_id": [
        f"DL{i:05d}" for i in range(1, len(delivered_orders) + 1)
    ],
    "order_id": delivered_orders["order_id"].to_numpy(),
    "driver_id": drivers["driver_id"].to_numpy()[delivery_driver_indices],
    "delivery_distance_km": delivered_orders[
        "delivery_distance_km"
    ].to_numpy(),
    "delivery_time_minutes": delivered_orders[
        "delivery_time_minutes"
    ].to_numpy(),
    "delivery_status": "Delivered"
})

# --------------------------------------------------
# 6. PAYMENTS
# One payment record per order, including cancelled orders.
# --------------------------------------------------
tip_amount = np.round(
    np.maximum(
        0,
        orders["order_amount"].to_numpy()
        * rng.choice([0, 0.05, 0.10, 0.15], n_orders,
                     p=[0.20, 0.30, 0.35, 0.15])
        + rng.normal(0, 8, n_orders)
    ),
    2
)

payments = pd.DataFrame({
    "payment_id": [f"P{i:05d}" for i in range(1, n_orders + 1)],
    "order_id": orders["order_id"],
    "payment_method": rng.choice(
        ["UPI", "Card", "Cash", "Wallet"], n_orders
    ),
    "order_amount": orders["order_amount"],
    "tip_amount": tip_amount,
    "payment_status": np.where(
        orders["order_status"] == "Cancelled",
        "Refunded",
        "Paid"
    )
})

# --------------------------------------------------
# 7. REVIEWS
# One review for a sample of delivered orders.
# Synthetic labels are illustrative, not human-annotated.
# --------------------------------------------------
review_count = min(7000, len(delivered_orders))
reviewed_orders = delivered_orders.sample(
    n=review_count,
    random_state=42
).reset_index(drop=True)

review_texts = [
    ("Excellent food and very quick delivery", "Positive"),
    ("Food was delicious and arrived on time", "Positive"),
    ("Great experience, everything was perfect", "Positive"),
    ("Delivery was late and food was cold", "Negative"),
    ("Order arrived late and packaging was damaged", "Negative"),
    ("Poor experience, missing items from my order", "Negative"),
    ("Food was okay, nothing special", "Neutral"),
    ("Average service and acceptable food", "Neutral"),
    ("Delivery was fine but the food was average", "Neutral")
]

review_choices = rng.integers(0, len(review_texts), review_count)

reviews = pd.DataFrame({
    "review_id": [f"RV{i:05d}" for i in range(1, review_count + 1)],
    "order_id": reviewed_orders["order_id"].to_numpy(),
    "customer_id": reviewed_orders["customer_id"].to_numpy(),
    "restaurant_id": reviewed_orders["restaurant_id"].to_numpy(),
    "review_text": [review_texts[i][0] for i in review_choices],
    "sentiment_label": [review_texts[i][1] for i in review_choices],
    "review_rating": [
        {"Positive": 5, "Neutral": 3, "Negative": 1}[
            review_texts[i][1]
        ] for i in review_choices
    ]
})

# --------------------------------------------------
# SAVE ALL DATASETS
# --------------------------------------------------
datasets = {
    "customers.csv": customers,
    "restaurants.csv": restaurants,
    "drivers.csv": drivers,
    "orders.csv": orders,
    "deliveries.csv": deliveries,
    "payments.csv": payments,
    "reviews.csv": reviews
}

for filename, df in datasets.items():
    df.to_csv(OUTPUT_DIR / filename, index=False)
    print(f"{filename}: {df.shape[0]} rows, {df.shape[1]} columns")

print("\nSynthetic datasets generated successfully.")
