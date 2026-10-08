a = int(input("Начальное число: "))
b = int(input("Конечное число: "))
step = 1 if a <= b else -1

for i in range(a, b + step, step):
    print(i)