s = input("Введите текст: ")
i = 0

for word in s.split():
    word = word.strip(".,!?;:")
    word = word.lower()

    if not word or "а" in word:
        continue

    print(word)
    i += 1

if not i:
    print("Нет совпадений")
print(f"Количество: {i}")