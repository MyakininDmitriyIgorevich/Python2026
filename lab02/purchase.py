price = int(input("Введите цену товара ₽: "))
count = int(input("Введите количество товара: "))
paid = int(input("Введите оплачиваемую сумму ₽: "))
cost = price * count
remainder = paid - cost

print(f"Стоимость: {cost}₽")
print(f"Сдача: {remainder}₽")