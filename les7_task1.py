"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""
import random


def bubble(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                continue
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


SIZE = 25
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

print(bubble(array))
