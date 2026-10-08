num = int(input("Уровень игрового ресурса (от 0 до 100): "))
year = int(input("Год (от 1 до 9999): "))

if num < 0 or num > 100:
    print("Ошибка диапазона")
else:
    if num <= 14:
        print("Пополнить")
    elif num <= 59:
        print("Достаточно")
    elif num <= 100:
        print("Большой запас")

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Да")
else:
    print("Нет")