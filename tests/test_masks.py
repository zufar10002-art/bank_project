import pytest

from src.masks import mask_account_number, mask_card_number


def test_mask_card_number():
    """Тест маскировки номера карты"""
    assert mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_account_number():
    """Тест маскировки номера счета"""
    assert mask_account_number("73654108430135874305") == "**4305"


def test_mask_card_number_invalid_length():
    """Тест на неверную длину номера карты"""
    with pytest.raises(ValueError):
        mask_card_number("123")


def test_mask_account_number_short():
    """Тест на слишком короткий номер счета"""
    with pytest.raises(ValueError):
        mask_account_number("123")
