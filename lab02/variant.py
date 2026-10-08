from math import pi

total = int(input("Общий объем: "))
capacity = int(input("Вместимость: "))
radius = float(input("Радиус: "))

filled = total // capacity
remainder = total % capacity
min_units = (total + capacity - 1) // capacity
circle_len = pi * radius * 2
circle_area = pi * radius ** 2

print(f"Полных: {filled}")
print(f"Остаток: {remainder}")
print(f"Всего: {min_units}")
print(f"Длина окружности: {circle_len:.2f}")
print(f"Площадь круга: {circle_area:.2f}")