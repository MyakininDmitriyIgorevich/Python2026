rejected = 0

while True:
    x = int(input("Введите целое число: "))
    if x > 0:
        break
    rejected += 1

print(f"Квадрат: {x ** 2}")
print(f"Отклонено: {rejected}")