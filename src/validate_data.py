
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/synthetic")

customers = pd.read_csv(DATA_DIR / "customers.csv")
restaurants = pd.read_csv(DATA_DIR / "restaurants.csv")
drivers = pd.read_csv(DATA_DIR / "drivers.csv")
orders = pd.read_csv(DATA_DIR / "orders.csv")
deliveries = pd.read_csv(DATA_DIR / "deliveries.csv")
reviews = pd.read_csv(DATA_DIR / "reviews.csv")
payments = pd.read_csv(DATA_DIR / "payments.csv")

datasets = {
    "customers": (customers, "customer_id"),
    "restaurants": (restaurants, "restaurant_id"),
    "drivers": (drivers, "driver_id"),
    "orders": (orders, "order_id"),
    "deliveries": (deliveries, "delivery_id"),
    "reviews": (reviews, "review_id"),
    "payments": (payments, "payment_id")
}

print("DATA QUALITY REPORT")
print("=" * 40)

for name, (df, key) in datasets.items():
    print(f"\n{name.upper()}")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Duplicate IDs:", df[key].duplicated().sum())
    print("Missing values:", df.isnull().sum().sum())

# Foreign-key checks
checks = {
    "Orders -> Customers":
        orders["customer_id"].isin(customers["customer_id"]).all(),
    "Orders -> Restaurants":
        orders["restaurant_id"].isin(restaurants["restaurant_id"]).all(),
    "Deliveries -> Orders":
        deliveries["order_id"].isin(orders["order_id"]).all(),
    "Deliveries -> Drivers":
        deliveries["driver_id"].isin(drivers["driver_id"]).all(),
    "Reviews -> Orders":
        reviews["order_id"].isin(orders["order_id"]).all(),
    "Payments -> Orders":
        payments["order_id"].isin(orders["order_id"]).all()
}

print("\nRELATIONSHIP CHECKS")
for name, passed in checks.items():
    print(f"{name}: {'PASS' if passed else 'FAIL'}")

assert all(df[key].is_unique for df, key in datasets.values()), \
    "Duplicate primary keys found."

assert all(checks.values()), \
    "Invalid foreign-key relationships found."

assert len(payments) == len(orders), \
    "Expected one payment record per order."

assert deliveries["order_id"].is_unique, \
    "Duplicate delivery records found."

assert set(deliveries["order_id"]).issubset(
    set(orders.loc[orders["order_status"] == "Delivered", "order_id"])
), "A delivery exists for a non-delivered order."

print("\nValidation completed successfully.")
