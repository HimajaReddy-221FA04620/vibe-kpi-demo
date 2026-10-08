from src.kpi_city import city_kpi


def test_mumbai_kpi_returns_expected_metrics():
    result = city_kpi("Mumbai")

    assert result is not None
    assert result["customer_count"] == 4
    assert result["average_monthly_spend"] == 139.3725
    assert result["churn_rate"] == 0.25


def test_injection_attempt_does_not_return_all_customers():
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result is None
