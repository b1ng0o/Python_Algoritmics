"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
import random


def merge_sort(arr):
    def merge(first, second):
        i = 0
        j = 0
        res = []
        while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                res.append(first[i])
                i += 1
            else:
                res.append(second[j])
                j += 1
        res += first[i:] + second[j:]
        return res

    if len(arr) <= 1:
        return arr
    else:
        pivot = len(arr) // 2
        first_list = arr[:pivot]
        second_list = arr[pivot:]
        return merge(merge_sort(first_list), merge_sort(second_list))


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [round((random.random() * MAX_ITEM), 3) for i in range(SIZE)]
print(array)

print(merge_sort(array))
