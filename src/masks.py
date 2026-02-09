"""Модуль для маскировки номеров карт и счетов."""


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Args:
        card_number (str): Номер карты (16 цифр)

    Returns:
        str: Маскированный номер в формате XXXX XX** **** XXXX
    """
    if not card_number:
        raise ValueError("Номер карты не может быть пустым")
    
    clean_number = ''.join(filter(str.isdigit, card_number))
    
    if len(clean_number) != 16:
        raise ValueError(f"Номер карты должен содержать 16 цифр")
    
    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер банковского счета.

    Args:
        account_number (str): Номер счета

    Returns:
        str: Маскированный номер в формате **XXXX
    """
    if not account_number:
        raise ValueError("Номер счета не может быть пустым")
    
    clean_number = ''.join(filter(str.isdigit, account_number))
    
    if len(clean_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    
    return f"**{clean_number[-4:]}"