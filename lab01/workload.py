first_subject = input("Название 1-го предмета: ")
num_of_lessons_1 = int(input("\tКол-во занятий за неделю: "))
duration_of_lesson_1 = int(input("\tПродолжительность занятия (мин.): "))

second_subject = input("Название 2-го предмета: ")
num_of_lessons_2 = int(input("\tКол-во занятий за неделю: "))
duration_of_lesson_2 = int(input("\tПродолжительность занятия (мин.): "))

available_hours = int(input("Доступное время на неделю (ч.): "))
total_load = duration_of_lesson_1 * num_of_lessons_1 + duration_of_lesson_2 * num_of_lessons_2
total_load_hours = total_load / 60
remainder_hours = available_hours - total_load_hours

print("\n---------- УЧЕБНАЯ НАГРУЗКА ----------")
print(f"{first_subject}: {num_of_lessons_1 * duration_of_lesson_1} мин.")
print(f"{second_subject}: {num_of_lessons_2 * duration_of_lesson_2} мин.")
print(f"Общая нагрузка: {total_load} м. или {total_load_hours:.2f} ч.")
print(f"Остаток свободного времени: {remainder_hours:.2f} ч.")
print(f"Нагрузка за 4 одинаковые недели: {total_load_hours * 4:.2f} ч.")
print("------------------------------------")