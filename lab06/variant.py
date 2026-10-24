numbers = []
for number in input("Введите целые числа через пробел: ").split():
    numbers.append(int(number))

print(f"Исходный список: {numbers}")

without_repeating = numbers.copy()
for i1, v1 in enumerate(without_repeating):
    for i2, v2 in enumerate(without_repeating):
        if v1 == v2 and i1 != i2:
            without_repeating.pop(i2)

print(f"Список без повторов: {without_repeating}")

new_nums = []
for num in numbers:
    if num:
        new_nums.append(num)

new_nums.sort()

print(f"Новый список: {new_nums}")
print(f"Количество: {len(new_nums)}")
print(f"Сумма: {sum(new_nums)}")