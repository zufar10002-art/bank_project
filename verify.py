"""Проверка работы функций виджета."""

from src.widget import mask_account_card, get_date

def test_all_examples():
    """Тестирует все примеры из задания."""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ ИЗ ЗАДАНИЯ")
    print("=" * 60)
    
    # Пример 1: Карта
    print("\n1. Маскировка карты:")
    input_card = "Visa Platinum 7000792289606361"
    result_card = mask_account_card(input_card)
    print(f"   Вход:  {input_card}")
    print(f"   Выход: {result_card}")
    
    # Пример 2: Счет
    print("\n2. Маскировка счета:")
    input_account = "Счет 73654108430135874305"
    result_account = mask_account_card(input_account)
    print(f"   Вход:  {input_account}")
    print(f"   Выход: {result_account}")
    
    # Пример 3: Дата
    print("\n3. Форматирование даты:")
    input_date = "2024-03-11T02:26:18.671407"
    result_date = get_date(input_date)
    print(f"   Вход:  {input_date}")
    print(f"   Выход: {result_date}")
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 60)

if __name__ == "__main__":
    test_all_examples()