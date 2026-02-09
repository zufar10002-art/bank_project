"""Основной файл программы."""

from src.widget import mask_account_card, get_date


def main():
    print("Тестирование функций:")
    print("=" * 50)
    
    # Тест маскировки
    tests = [
        "Visa Platinum 7000792289606361",
        "Счет 73654108430135874305",
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758"
    ]
    
    print("\n1. Маскировка карт и счетов:")
    for test in tests:
        result = mask_account_card(test)
        print(f"Ввод:  {test}")
        print(f"Вывод: {result}\n")
    
    # Тест даты
    print("\n2. Форматирование даты:")
    date_test = "2024-03-11T02:26:18.671407"
    date_result = get_date(date_test)
    print(f"Ввод:  {date_test}")
    print(f"Вывод: {date_result}")


if __name__ == "__main__":
    main()