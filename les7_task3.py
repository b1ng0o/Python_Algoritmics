"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы."""
import random
from statistics import median


m = int(input("Введите натуральное число: "))
size = int(2 * m + 1)
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
median_in_list = median(array)
print(f'Медиана списка {array=} - {median_in_list}')

