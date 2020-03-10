"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""
import timeit
import cProfile


def my_func(a):
    n = 100
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    sieve = set(sieve)
    sieve.discard(0)
    sieve = list(sieve)
    res = sieve[a - 1]
    return res


print(timeit.timeit('my_func(2)', number=500, globals=globals()))  # 0.0163236
print(timeit.timeit('my_func(4)', number=500, globals=globals()))  # 0.020269399999999993
print(timeit.timeit('my_func(7)', number=500, globals=globals()))  # 0.021351399999999993
print(timeit.timeit('my_func(11)', number=500, globals=globals()))  # 0.017210000000000017
cProfile.run('my_func(5)')  # 1    0.000    0.000    0.000    0.000 les4_task2.py:7(<listcomp>)


# print(my_func(2))


def my_func1(a):
    n = 100
    my_list = []
    for i in range(2, n):
        for j in range(2, int((pow(i, .5))) + 1):
            if i % j == 0:
                break
        else:
            my_list.append(i)
    res = my_list[a - 1]
    return res


print(timeit.timeit('my_func1(2)', number=500, globals=globals()))  # 0.04789850000000001
print(timeit.timeit('my_func1(4)', number=500, globals=globals()))  # 0.04760250000000002
print(timeit.timeit('my_func1(5)', number=500, globals=globals()))  # 0.044364600000000004
print(timeit.timeit('my_func1(7)', number=500, globals=globals()))  # 0.04921059999999999
cProfile.run('my_func1(2)')  # 98    0.000    0.000    0.000    0.000 {built-in method builtins.pow}
# print(my_func1(7))

"""Вывод
Только с этой задачей понял решето Эратосфена и простые числа, почувствовал себя тупым) но потом все таки понял.
Для себя отметил: на удивление первый вариант отрабатывает быстрее, хотя я предпологал что засунув туда изменение списка
в множество, удаление 0, и обратное преоразование в список, займет больше времени, однако хождение по 2 циклам оказалось
затратнее по времени.
"""