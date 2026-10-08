total_seconds = int(input("Введите кол-во секунд: "))
hours = total_seconds // 60 // 60 # с -> мин -> ч
minutes = total_seconds % (60 ** 2) // 60 # Берём остаток от часов и переводим секунды в минуты
seconds = total_seconds % 60 # Каждый час имеет 60 минут, каждая минута имеет 60 секунд, поэтому остаток от деления на 60 даст нам количество секунд
print(f"{hours} ч {minutes} мин {seconds} сек")