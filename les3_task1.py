"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

SIZE_MIN = 2 
SIZE_MAX = 10
MIN_ITEM = 2
MAX_ITEM = 100
ARRAY_ITEM = 0
array = [ARRAY_ITEM for _ in range(SIZE_MIN, SIZE_MAX)]
count = 0

for i in range(MIN_ITEM, MAX_ITEM):
    for j in range(SIZE_MIN, SIZE_MAX):
        if i % j == 0:
            array[j - 2] += 1
while count < len(array):
    print(f'Чисел кратных {count + 2}: {array[count]}')
    count += 1
