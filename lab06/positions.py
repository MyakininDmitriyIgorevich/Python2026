numbers = []
for number in input("Введите целые числа через пробел: ").split():
    numbers.append(int(number))

if not numbers:
    print("Нет данных")
else:
    idxs = []
    max_val = max(numbers)
    for idx, val in enumerate(numbers):
        if val == max_val:
            idxs.append(idx)

    print(f"Список индексов: {idxs}")