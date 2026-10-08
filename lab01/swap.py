first_room = input("Введите название 1-ой аудитории: ")
second_room = input("Введите название 2-ой аудитории: ")

print(f"first_room: {first_room}, second_room: {second_room}")

third_room = first_room
first_room = second_room
second_room = third_room

print(f"first_room: {first_room}, second_room: {second_room}")