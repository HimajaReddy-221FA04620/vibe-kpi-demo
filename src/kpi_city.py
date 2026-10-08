from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> dict[str, float | int] | None:
    """Return customer count, average spend, and churn rate for one city."""
    with sqlite3.connect(DB_PATH) as connection:
        row = connection.execute(
            """SELECT COUNT(*) AS customer_count,
                      AVG(monthly_spend) AS average_monthly_spend,
                      AVG(churned) AS churn_rate
               FROM customers_raw
               WHERE city = ?""",
            (city,),
        ).fetchone()

    customer_count, average_spend, churn_rate = row
    if customer_count == 0:
        print(f"No customers found for {city!r}.")
        return None

    result = {
        "customer_count": customer_count,
        "average_monthly_spend": average_spend,
        "churn_rate": churn_rate,
    }
    print(f"{city}: {result}")
    return result


if __name__ == "__main__":
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
