order_name = input("Название заказа: ")
order_author = input("Имя заказчика: ")

print("Первый товар:")
first_name = input("\tНазвание: ")
first_count = int(input("\tКоличество: "))
first_price = float(input("\tЦена ₽: "))
first_cost = first_price * first_count

print("Второй товар:")
second_name = input("\tНазвание: ")
second_count = int(input("\tКоличество: "))
second_price = float(input("\tЦена ₽: "))
second_cost = second_price * second_count

coupon = int(input("Скидка %: "))
delivery_cost = float(input("Стоимость доставки ₽: "))
goods_price = first_price + second_price
goods_count = first_count + second_count
goods_cost = first_cost + second_cost
coupon_cost = goods_cost * coupon / 100
total_cost = goods_cost - coupon_cost + delivery_cost
amount_deposited = float(input("Внесённая сумма ₽: "))
remainder = amount_deposited - total_cost

print(f"\n---------- {order_name} ({order_author}) ----------\n")
print("* Товары", f"* Кол-во", f"* Цена/шт.", f"* Стоимость", sep = " | ")
print(f"------------------------------------------------------------");
print(first_name, f"{first_count} шт.", f"{first_price:.2f}₽", f"{first_cost:.2f}₽", sep = " | ")
print(second_name, f"{second_count} шт.", f"{second_price:.2f}₽", f"{second_cost:.2f}₽", sep = " | ")
print(f"------------------------------------------------------------");
print(f"Сумма: {goods_cost:.2f}₽")
print(f"Скидка: {coupon_cost:.2f}₽")
print(f"Стоимость доставки: {delivery_cost:.2f}₽")
print(f"Итого: {total_cost:.2f}₽")
print(f"Внесённая сумма: {amount_deposited:.2f}₽")
print(f"Сдача: {remainder:.2f}₽")