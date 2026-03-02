import pytest

from src.widget import get_date, mask_account_card


# Параметризация для mask_account_card
@pytest.mark.parametrize("input_str, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("MasterCard 1234567890123456", "MasterCard 1234 56** **** 3456"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 12345", "Счет **2345"),
    ("Visa 1234", "Visa 1234 **** **** 1234"),
    ("", ""),
    ("   ", "   "),
    ("JustText", "JustText"),
    ("Visa7000792289606361", "Visa7000792289606361"),
])
def test_mask_account_card_param(input_str, expected):
    """Параметризованный тест mask_account_card"""
    assert mask_account_card(input_str) == expected


# Параметризация для get_date
@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11", "11.03.2024"),
    ("2024-03-11 12:30:45", "11.03.2024"),
    ("11.03.2024", "11.03.2024"),
    ("", ""),
    ("не дата", "не дата"),
    ("2024/03/11", "2024/03/11"),
])
def test_get_date_param(input_date, expected):
    """Параметризованный тест get_date"""
    assert get_date(input_date) == expected


# Дополнительные тесты для веток с ошибками
def test_mask_account_card_card_exception():
    """Тест обработки исключения для карты"""
    # Проверяем, что функция не падает с исключением
    result = mask_account_card("Visa 123")
    assert isinstance(result, str)


def test_mask_account_card_account_exception():
    """Тест обработки исключения для счета"""
    result = mask_account_card("Счет 12")
    assert "**12" in result or result == "Счет 12"