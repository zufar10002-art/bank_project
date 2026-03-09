"""
Модуль виджета для обработки банковских операций.
"""

from datetime import datetime

from .masks import mask_account_number, mask_card_number


def mask_account_card(data_string: str) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        data_string (str): Строка типа "Visa Platinum 7000792289606361"

    Returns:
        str: Строка с маскированным номером
    """
    if not data_string:
        return ""
    parts = data_string.strip().split()
    if len(parts) < 2:
        return data_string
    account_type = " ".join(parts[:-1])
    number = parts[-1]
    if not number.isdigit():
        return data_string

    if account_type.lower() == "счет":
        try:
            masked_number = mask_account_number(number)
        except ValueError:
            if len(number) >= 4:
                masked_number = f"**{number[-4:]}"
            else:
                masked_number = f"**{number}"
    else:
        try:
            masked_number = mask_card_number(number)
        except ValueError:
            if len(number) == 16:
                masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
            elif len(number) >= 4:
                masked_number = f"{number[:4]} **** **** {number[-4:]}"
            else:
                masked_number = "**** **** **** ****"

    return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        str: Дата в формате "11.03.2024"
    """
    if not date_string:
        return ""

    try:
        if '.' in date_string:
            date_part = date_string.split('.')[0]
        else:
            date_part = date_string

        date_obj = datetime.fromisoformat(date_part)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        formats_to_try = [
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%d.%m.%Y"
        ]

        for fmt in formats_to_try:
            try:
                date_obj = datetime.strptime(date_string, fmt)
                return date_obj.strftime("%d.%m.%Y")
            except ValueError:
                continue

        return date_string
    except Exception:
        return date_string
