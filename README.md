# Bank Project

## Описание
Проект для маскировки банковских карт и счетов, обработки транзакций.  
Реализованы функции для скрытия конфиденциальных данных и работы со списками операций.

---

## Функции

### Модуль `masks`
- `mask_card_number(card_number: str) -> str`  
  Маскирует номер карты в формат: `XXXX XX** **** XXXX`
- `mask_account_number(account_number: str) -> str`  
  Маскирует номер счёта в формат: `**XXXX`

### Модуль `widget`
- `mask_account_card(data_string: str) -> str`  
  Принимает строку с типом и номером (например, "Visa Platinum 7000792289606361"),  
  возвращает строку с замаскированным номером.
- `get_date(date_string: str) -> str`  
  Преобразует дату из ISO формата (`2024-03-11T02:26:18.671407`)  
  в формат `ДД.ММ.ГГГГ` (`11.03.2024`).

### Модуль `processing`
- `filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]`  
  Фильтрует список транзакций по заданному статусу.
- `sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]`  
  Сортирует транзакции по дате (по убыванию или возрастанию).

---

## Установка и зависимости

### Требования
- Python 3.14+
- Установка зависимостей:

```bash
pip install pytest pytest-cov flake8 mypy isort