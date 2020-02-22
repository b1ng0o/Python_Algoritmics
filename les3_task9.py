"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.


-- честно пытался вывести отформатированную матрицу, так и не смог преобразовать ваш кусок кода, под свой
начал понимать как, но времени не хватило
сильно мелом не кидайтесь) сдал по раньше, потому что потом времени не будет,
так как переезд в другой город и новая работа, а сдавать аж к следующим выходным не хотелось бы
"""

import random

SIZE1 = 10
SIZE2 = 5
MIN_ITEM = 0
MAX_ITEM = 50
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE1)] for _ in range(SIZE2)]
max_element = 0

for line in array:
    print(line)
    for i, item in enumerate(line):
        print(f'{item:>6}', end='')
    print()

for i in range(SIZE2):
    min_element = MAX_ITEM
    for j in range(SIZE1):
        if array[i][j] < min_element:
            min_element = array[i][j]
        if max_element < min_element:
            max_element = min_element
print(f'Максимальный среди минимальных - {max_element}')

