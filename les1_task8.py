"""
Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""

print("Узнайте вискосный ли год")
year = int(input("Введите натуральное число"))
if year % 400 == 0:
    print("Високосный")
elif year % 100 != 0:
    if year % 4 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Обычный")
