import pandas as pd
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

products = {
    "Electronics": {
        "Headphones": 1500,
        "Keyboard": 1200,
        "Speaker": 2000,
        "Mouse": 700
    },
    "Clothing": {
        "T-Shirt": 500,
        "Jeans": 1200,
        "Jacket": 1800,
        "Shirt": 900
    },
    "Beauty": {
        "Face Wash": 250,
        "Shampoo": 300,
        "Moisturizer": 450
    },
    "Home": {
        "Mixer": 2500,
        "Cookware": 1800,
        "Bedsheet": 1000
    },
    "Sports": {
        "Yoga Mat": 800,
        "Football": 600,
        "Sports Shoes": 2200
    }
}

regions = ["North", "South", "East", "West"]

records = []
start_date = datetime(2025, 1, 1)

for i in range(1, 251):
    category = random.choice(list(products.keys()))
    product = random.choice(list(products[category].keys()))

    quantity = random.randint(1, 5)
    unit_price = products[category][product]

    sales = quantity * unit_price
    cost = int(sales * random.uniform(0.55, 0.80))
    profit = sales - cost

    order_date = start_date + timedelta(days=random.randint(0, 364))

    records.append({
        "Order_ID": f"ORD{i:03}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Region": random.choice(regions),
        "Category": category,
        "Product": product,
        "Quantity": quantity,
        "Unit_Price": unit_price,
        "Sales": sales,
        "Cost": cost,
        "Profit": profit
    })

df = pd.DataFrame(records)

output_path = Path(__file__).parent / "data" / "retail_sales.csv"
output_path.parent.mkdir(exist_ok=True)

df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print("Total sales: ₹", df["Sales"].sum())
print("Total profit: ₹", df["Profit"].sum())