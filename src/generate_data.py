import random
import uuid
from datetime import datetime, timedelta, date
from pathlib import Path

import pandas as pd

# Folder where we will write generated CSV files
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def gen_customers(n: int = 500) -> pd.DataFrame:
    """Generate customer master data."""
    return pd.DataFrame({
        "customer_id": [uuid.uuid4() for _ in range(n)],
        "signup_date": [date.today() - timedelta(days=random.randint(1, 1200)) for _ in range(n)],
        "country": [random.choice(["US", "IN", "CA", "UK"]) for _ in range(n)],
    })

def gen_merchants(n: int = 100) -> pd.DataFrame:
    """Generate merchant master data."""
    return pd.DataFrame({
        "merchant_id": [uuid.uuid4() for _ in range(n)],
        "category": [random.choice(["grocery", "fuel", "online", "travel", "pharmacy"]) for _ in range(n)],
        "risk_tier": [random.choice(["low", "medium", "high"]) for _ in range(n)],
    })

def gen_transactions(customers: pd.DataFrame, merchants: pd.DataFrame, n: int = 20000, days: int = 60) -> pd.DataFrame:
    """Generate transaction fact data linked to customers and merchants."""
    base = datetime.now() - timedelta(days=days)
    customer_ids = customers["customer_id"].tolist()
    merchant_ids = merchants["merchant_id"].tolist()

    rows = []
    for _ in range(n):
        rows.append({
            "tx_id": uuid.uuid4(),
            "customer_id": random.choice(customer_ids),
            "merchant_id": random.choice(merchant_ids),
            "tx_time": base + timedelta(minutes=random.randint(0, days * 24 * 60)),
            "amount": round(random.uniform(1, 500), 2),
            "currency": "USD",
            "status": random.choice(["approved", "declined"]),
        })
    return pd.DataFrame(rows)

def main() -> None:
    customers = gen_customers()
    merchants = gen_merchants()
    tx = gen_transactions(customers, merchants)

    customers.to_csv(DATA_DIR / "customers.csv", index=False)
    merchants.to_csv(DATA_DIR / "merchants.csv", index=False)
    tx.to_csv(DATA_DIR / "transactions.csv", index=False)

    print("Generated:")
    print(" - data/customers.csv")
    print(" - data/merchants.csv")
    print(" - data/transactions.csv")

if __name__ == "__main__":
    main()
