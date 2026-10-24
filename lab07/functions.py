def sum_digits(number: int) -> int:
    number = number if number >= 0 else -number
    amount = 0

    for sub in str(number):
        amount += int(sub)

    return amount

def average(numbers: list[int]) -> int:
    if numbers:
        return sum(numbers) / len(numbers)

    return None

def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())

def select_numbers(numbers: list[int], threshold: int) -> list[int]:
    threshold = threshold if threshold >= 0 else -threshold

    new_nums = []
    for num in numbers:
        if (0 <= num <= threshold):
            new_nums.append(num)

    return new_nums

def is_palindrome(text: str) -> bool:
    if not text:
        return False

    lst = "".join(text.lower().split())

    if not lst:
        return False
    
    return lst == lst[::-1]
