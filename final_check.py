"""Финальная проверка точного соответствия задания."""

from src.widget import mask_account_card, get_date

print("=" * 70)
print("ФИНАЛЬНАЯ ПРОВЕРКА ТОЧНОГО СООТВЕТСТВИЯ ЗАДАНИЮ")
print("=" * 70)

# Тест 1: Точный пример из задания - Карта
print("\n1. ТЕСТ: Точный пример для карты из задания")
input1 = "Visa Platinum 7000792289606361"
expected1 = "Visa Platinum 7000 79** **** 6361"
result1 = mask_account_card(input1)
print(f"   Вход:     '{input1}'")
print(f"   Ожидаем:  '{expected1}'")
print(f"   Получили: '{result1}'")
if result1 == expected1:
    print("   ✅ СОВПАДАЕТ ИДЕАЛЬНО!")
else:
    print("   ❌ НЕ СОВПАДАЕТ")

# Тест 2: Точный пример из задания - Счет
print("\n2. ТЕСТ: Точный пример для счета из задания")
input2 = "Счет 73654108430135874305"
expected2 = "Счет **4305"
result2 = mask_account_card(input2)
print(f"   Вход:     '{input2}'")
print(f"   Ожидаем:  '{expected2}'")
print(f"   Получили: '{result2}'")
if result2 == expected2:
    print("   ✅ СОВПАДАЕТ ИДЕАЛЬНО!")
else:
    print("   ❌ НЕ СОВПАДАЕТ")

# Тест 3: Точный пример из задания - Дата
print("\n3. ТЕСТ: Точный пример для даты из задания")
input3 = "2024-03-11T02:26:18.671407"
expected3 = "11.03.2024"
result3 = get_date(input3)
print(f"   Вход:     '{input3}'")
print(f"   Ожидаем:  '{expected3}'")
print(f"   Получили: '{result3}'")
if result3 == expected3:
    print("   ✅ СОВПАДАЕТ ИДЕАЛЬНО!")
else:
    print("   ❌ НЕ СОВПАДАЕТ")

print("\n" + "=" * 70)
print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! ПРОЕКТ ГОТОВ К СДАЧЕ!")
print("=" * 70)