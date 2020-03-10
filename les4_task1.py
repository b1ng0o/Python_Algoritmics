"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import timeit
import cProfile

# Вариант 1

STAT_NUM = 1.0
num = 10


def sum_nums(n, m):
    sum_nums1 = 0
    for i in range(n):
        sum_nums1 += m
        m /= -2
    return sum_nums1


print(timeit.timeit('sum_nums(10, STAT_NUM)', number=1000, globals=globals()))  # 0.0016699999999999979

print(timeit.timeit('sum_nums(20, STAT_NUM)', number=1000, globals=globals()))  # 0.002457000000000001
print(timeit.timeit('sum_nums(40, STAT_NUM)', number=1000, globals=globals()))  # 0.004842300000000001
print(timeit.timeit('sum_nums(80, STAT_NUM)', number=1000, globals=globals()))  # 0.008859199999999998
print(timeit.timeit('sum_nums(160, STAT_NUM)', number=1000, globals=globals()))  # 0.017508999999999997
cProfile.run('sum_nums(10, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:14(sum_nums)
cProfile.run('sum_nums(20, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:14(sum_nums)
cProfile.run('sum_nums(40, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:14(sum_nums)
cProfile.run('sum_nums(80, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:14(sum_nums)


# Вариант 2
def sum_v2(n, m):
    sum_num = {
        1: 1,
        2: -0.5,
        3: 0.25,
    }
    if n in sum_num:
        return sum(sum_num.values())
    for i in range(len(sum_num) + 1, int(n) + 1):
        m = sum_num[len(sum_num)] / -2
        sum_num[i] = m
    return sum(sum_num.values())


print(timeit.timeit('sum_v2(10, STAT_NUM)', number=1000, globals=globals()))  # 0.0035488999999999937
print(timeit.timeit('sum_v2(20, STAT_NUM)', number=1000, globals=globals()))  # 0.005224599999999996
print(timeit.timeit('sum_v2(40, STAT_NUM)', number=1000, globals=globals()))  # 0.010550600000000007
print(timeit.timeit('sum_v2(80, STAT_NUM)', number=1000, globals=globals()))  # 0.019425600000000015
print(timeit.timeit('sum_v2(160, STAT_NUM)', number=1000, globals=globals()))  # 0.0390182
cProfile.run('sum_v2(10, STAT_NUM)')  # 8    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('sum_v2(20, STAT_NUM)')  # 18    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('sum_v2(40, STAT_NUM)')  # 38    0.000    0.000    0.000    0.000 {built-in method builtins.len}
cProfile.run('sum_v2(80, STAT_NUM)')  # 78    0.000    0.000    0.000    0.000 {built-in method builtins.len}


# Варинт 3
def sum_v3(n, m):
    s = {
        1: m,
    }
    for i in range(2, int(n) + 1):
        m = m / -2
        s[i] = m
    return sum(s.values())


print(timeit.timeit('sum_v3(10,STAT_NUM)', number=1000, globals=globals()))  # 0.0024776999999999993
print(timeit.timeit('sum_v3(20,STAT_NUM)', number=1000, globals=globals()))  # 0.004156899999999991
print(timeit.timeit('sum_v3(40,STAT_NUM)', number=1000, globals=globals()))  # 0.007356999999999975
print(timeit.timeit('sum_v3(80,STAT_NUM)', number=1000, globals=globals()))  # 0.01331779999999999
print(timeit.timeit('sum_v3(160,STAT_NUM)', number=1000, globals=globals()))  # 0.028168200000000004
cProfile.run('sum_v3(10, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:66(sum_v3)
cProfile.run('sum_v3(20, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:66(sum_v3)
cProfile.run('sum_v3(40, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:66(sum_v3)
cProfile.run('sum_v3(80, STAT_NUM)')  # 1    0.000    0.000    0.000    0.000 les2_task4.py:66(sum_v3)


"""Вывод
Пробовал несколько задач подобрать для этого задания. вывод cProfile везде был одинаков, вывод - думаю нужна более 
сложная задача, и наверное с рекурсией. В данном случае вариант 1 лучше, так как отрабатывает быстрее. Во всех
трех вариантах линейная зависимость. Итого: тему с измерением времени выполнения кода, и нахождения слабых мест кода
понял, буду пробовать использовать в других задачах.
"""