"""Модуль для обработки списков транзакций"""

from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список транзакций по статусу state"""
    return [item for item in transactions if item.get("state") == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует список транзакций по дате"""
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)