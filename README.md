# Applied Analytics mini project

This project loads a small customer CSV into SQLite and calculates city-level customer KPIs with a parameterized SQL query.

## Run the project

Run these commands from the project folder after activating `.venv`:

```powershell
python -m pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
python -m pytest
```

The KPI output includes customer count, average monthly spend, and churn rate. The second call passes an SQL injection attempt as a city name; parameterized SQL treats it as plain text, so it returns no matching customers.
