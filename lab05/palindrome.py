s = input("Введите текст: ")
lst = "".join(s.lower().split())

if not lst:
    print("Нет текста")
elif lst == lst[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")

# Альтернативное решение без обратного среза
# s = input("Введите текст: ")
# lst = "".join(s.lower().split())
# 
# if not lst:
#     print("Нет текста")
# else:
#     length = len(lst)
#     for i in range(length):
#         if lst[i] != lst[length - i - 1]:
#             print("Не палиндром")
#             length = 0
#             break
# 
#     if length:
#         print("Палиндром")