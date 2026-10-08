# Фрагмент А:
# first = "2"
# second = "3"
# print(first + second)
# Ожидаемый результат: 5. Причина ошибки: значения "2" и "3" являются
# строками, поэтому оператор + соединяет их и дает "23", а не складывает.
first = "2"
second = "3"
print("А, типы до преобразования:", type(first).__name__, type(second).__name__)
first_number = int(first)
second_number = int(second)
print("А, типы после преобразования:", type(first_number).__name__, type(second_number).__name__)
print("А, сумма:", first_number + second_number)


# Фрагмент Б
# age = input("Возраст: ")
# print(age + 1)
# Ожидаемый результат для ввода 17: 18. Причина ошибки: input() всегда
# возвращает строку, а к строке нельзя прибавить целое число 1.
age = input("Возраст: ")
print("Б, тип до преобразования:", type(age).__name__)
age_number = int(age)
print("Б, тип после преобразования:", type(age_number).__name__)
print("Б, возраст через год:", age_number + 1)


# Фрагмент В
# first = 4
# second = 7
# third = 10
# average = first + second + third / 3
# print(average)
# Ожидаемый результат: 7.0. Причина ошибки: без скобок сначала выполняется
# деление third / 3, поэтому нужно разделить на 3 всю сумму.
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("В, среднее:", average)