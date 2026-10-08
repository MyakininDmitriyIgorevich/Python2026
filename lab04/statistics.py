n = int(input("Введите положительное кол-во целых чисел: "))

while n < 1:
    n = int(input("Количество должно быть больше 1. Повторите ввод: "))

x = int(input(f"Введите число 1: "))
total = x
positive_count = 1 if x > 0 else 0
maximum = x

for i in range(2, n + 1):
    x = int(input(f"Введите число {i}: "))
    total += x
    if x > 0:
        positive_count += 1
    if x > maximum:
        maximum = x

print("Сумма:", total)
print("Число положительных:", positive_count)
print("Максимум:", maximum)