<div align = "center">

# «Функции»
## `main.py`
</div>

Команда запуска :
```text
python main.py
```
<table>
<tr>
<th>Входные данные</th>
<th>Ожидаемый результат</th>
<th>Фактический результат</th>
</tr>
<tr>
<td>

```text
Введите целое число: 0
Введите целые числа через пробел: -5 0 2 5
Введите порог: 2
Введите текст: Рвал дед лавр
```
</td>
<td>

```text
sum_digits: 0
average: 0.5
normalize_text: рвал дед лавр
select_numbers: [0, 2]
is_palindrome: True
```
</td>
<td>

```text
sum_digits: 0
average: 0.5
normalize_text: рвал дед лавр
select_numbers: [0, 2]
is_palindrome: True
```
</td>
</tr>
</table>
<div align = "center">

## `test_functions.py`
</div>

Команда запуска :
```text
python test_functions.py
```
Вывод :
```text
Базовые проверки пройдены
```
Если внести ошибку в функцию :
<table>
<tr>
<th>Исходная функция</th>
<th>Ошибочная функция</th>
</tr>
<tr>
<td>

```python
def average(numbers: list[int]) -> int:
    if numbers:
        return sum(numbers) / len(numbers)

    return None
```
</td>
<td>

```python
def average(numbers: list[int]) -> int:
    if numbers:
        return sum(numbers) * len(numbers)

    return None
```
</td>
</tr>
</table>

То при запуске выйдет исключение `AssertionError` :
```python
from functions import average, normalize_text, sum_digits, select_numbers, is_palindrome

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4 # AssertionError
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
assert select_numbers([-5, 0, 2, 5], 2) == [0, 2]
assert select_numbers([], 2) == []
assert select_numbers([-3, -2, -1, 0, 1, 2, 3], 2) == [0, 1, 2]
assert is_palindrome("А роза упала на лапу Азора") == True
assert is_palindrome("а    ") == True
assert is_palindrome(" ") == False
assert is_palindrome("Python") == False
assert is_palindrome("А!") == False
print("Базовые проверки пройдены")
```