"""
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
print("Введите три различных целых числа")
num1 = int(input("Введите целое число1: "))
num2 = int(input("Введите целое число2: "))
num3 = int(input("Введите целое число3: "))
if num2 > num1 > num3 or num2 < num1 < num3:
    print(f'Среднее число 1 {num1= }')
elif num1 > num2 > num3 or num1 < num2 < num3:
    print(f'Среднее число 2 {num2= }')
else:
    print(f'Среднее число 3 {num3= }')
