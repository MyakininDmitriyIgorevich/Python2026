first = int(input("Первое число: "))
second = int(input("Второе число: "))
third = int(input("Третье число: "))

print("Минимальное число: ", end = "")
if first < second:
    if first < third:
        print(first)
    else:
        print(third)
elif second < third:
    print(second)
else:
    print(third)