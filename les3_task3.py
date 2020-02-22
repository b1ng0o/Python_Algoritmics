"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_min = 0
array_max = 0
for i in range(SIZE):
    if array[i] < array[array_min]:
        array_min = i
    elif array[i] > array[array_max]:
        array_max = i
array[array_min], array[array_max] = array[array_max], array[array_min]
print(array)
print(f'Минимальное число из списка: {array[array_max]}, Максимальное число: {array[array_min]}')


