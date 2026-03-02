import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-15"},
        {"id": 2, "state": "CANCELED", "date": "2023-02-20"},
        {"id": 3, "state": "EXECUTED", "date": "2023-03-10"},
    ]


def test_filter_by_state(sample_transactions):
    """Тест фильтрации по умолчанию (EXECUTED)"""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(sample_transactions):
    """Тест фильтрации по CANCELED"""
    result = filter_by_state(sample_transactions, "CANCELED")
    assert len(result) == 1
    assert result[0]["state"] == "CANCELED"


def test_filter_by_state_not_found(sample_transactions):
    """Тест фильтрации по несуществующему статусу"""
    result = filter_by_state(sample_transactions, "PENDING")
    assert result == []


def test_sort_by_date_desc(sample_transactions):
    """Тест сортировки по убыванию"""
    result = sort_by_date(sample_transactions)
    assert result[0]["date"] == "2023-03-10"
    assert result[-1]["date"] == "2023-01-15"


def test_sort_by_date_asc(sample_transactions):
    """Тест сортировки по возрастанию"""
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["date"] == "2023-01-15"
    assert result[-1]["date"] == "2023-03-10" 
