numbers = []
for number in input("Введите целые числа через пробел: ").split():
    numbers.append(int(number))

nums_abs = []
for num in numbers:
    nums_abs.append(num if num >= 0 else -num)

print(f"Исходный список: {numbers}")
print(f"Новый список: {nums_abs}")