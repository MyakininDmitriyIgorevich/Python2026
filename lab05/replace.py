s = input("Введите текст: ")
sub_count = s.count(":")
replaced = s.replace(":", "-")

print(f"Новый текст: {replaced}")
print(f"Количество замен: {sub_count}")