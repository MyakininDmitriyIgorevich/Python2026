n = int(input("Введите положительное кол-во целых чисел: "))

if n < 0:
    print("Ошибка: количество должно быть больше нуля")
else:
    count = 0
    total = 0

    for i in range(n):
        x = int(input(f"Введите число {i + 1}: "))

        if x != 0:
            count += 1
            total += x

    print("Количество:", count)
    print("Сумма:", total)

for N in [2, 9, 17, 49]:
    divisor = 2

    if N >= 2:
        while divisor ** 2 <= N:
            if N % divisor == 0:
                print(f"{N} — составное")
                break
            divisor += 1
        else:
            print(f"{N} — простое")
    else:
        print(f"{N} — составное")