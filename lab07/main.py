import functions

def main():
    num = int(input("Введите целое число: "))
    lst = [int(sub) for sub in input("Введите целые числа через пробел: ").split()]
    threshold = int(input("Введите порог: "))
    s = input("Введите текст: ")

    print(f"sum_digits: {functions.sum_digits(num)}")
    print(f"average: {functions.average(lst)}")
    norm_text = functions.normalize_text(s)
    print(f"normalize_text: {norm_text if norm_text else "Нет данных"}")
    print(f"select_numbers: {functions.select_numbers(lst, threshold)}")
    print(f"is_palindrome: {functions.is_palindrome(s)}")

if __name__ == "__main__":
    main()