"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_min = 0
array_max = 0
sum_element = 0
for i in range(SIZE):
    if array[i] < array[array_min]:
        array_min = i
    elif array[i] > array[array_max]:
        array_max = i
if array_min > array_max:
    array_min, array_max = array_max, array_min
for i in range(array_min + 1, array_max):
    sum_element += array[i]
out_str = f'Сумма элементов между максимальным и минимальным элементами = {sum_element}'
print(f'{out_str}' if sum_element != 0 else f'{out_str}, так как между ними нет других элементов')
