from pathlib import Path
import sqlite3

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "raw" / "customers_raw.csv"
DB_PATH = ROOT / "data" / "db" / "analytics.db"


def load_customers() -> int:
    """Load the raw customer CSV into SQLite, replacing the table each run."""
    customers = pd.read_csv(CSV_PATH, dtype={"customer_id": "int64", "city": "string", "monthly_spend": "float64", "churned": "int64"})
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS customers_raw (
                customer_id INTEGER,
                city TEXT,
                monthly_spend REAL,
                churned INTEGER CHECK (churned IN (0, 1))
            )"""
        )
        customers.to_sql("customers_raw", connection, if_exists="replace", index=False)

    return len(customers)


if __name__ == "__main__":
    row_count = load_customers()
    print(f"Loaded {row_count} customers into {DB_PATH}")
