# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
n = 1
for fruit in fruits:
    print(n, '.' + '{:>12}'.format(fruit))
    n += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
from typing import List

fruits = ['apple', 'bananas', 'kiwi', 'watermelon', 'melon']
berrys = ['watermelon', 'raspberry', 'strawberry', 'blackberry', 'melon', 'blueberry', 'wild strawberry']
result = list(set(fruits) - set(berrys))
print(result)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = []
for digit in numbers:
    if digit % 2 == 0:
        digit = digit/4
    else:
        digit = digit * 2
    new_numbers.append(digit)
print(new_numbers)