"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
import hashlib

user_str = 'sova'


def my_hash(st):
    sets = set()
    for i in range(len(st)):
        for j in range(len(st), i, -1):
            if st[i:j] != st and st != '':
                sets.add(hashlib.sha1(st[i:j].encode('UTF-8')).hexdigest())
    return f'{len(sets)}'


print(my_hash(user_str))
