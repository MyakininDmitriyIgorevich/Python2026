numbers = []
for number in input("Введите целые числа через пробел: ").split():
    numbers.append(int(number))

length = len(numbers)

if not length:
    print("Нет данных")
else:
    amount = sum(numbers);
    print(f"Количество: {length}")
    print(f"Сумма: {amount}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {amount / length:.2f}")