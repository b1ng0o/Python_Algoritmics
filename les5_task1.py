"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий,чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple

count_company = int(input('Введите целое число - количество компаний: '))
Company = namedtuple('Company', 'name, profit1, profit2, profit3, profit4, total')
company_list = []
total_profit = 0
for i in range(count_company):
    profit = []
    name = input(f'Введите название {i + 1} компании:')
    for j in range(4):
        profit.append(float(input(f'Прибыл за {j + 1} квартал: ')))

    company_list.append(Company(name, *profit, sum(profit)))

    total_profit += sum(profit)

print(f'Общая прибыль компаний за 4 вартала составила: {total_profit}')

avg_profit = total_profit / count_company
print(f'Средняя прибыль компаний: {avg_profit}')

for i in company_list:
    if i.total > avg_profit:
        print(f'У компании {i.name} прибыль выше средней прибыли компаний')
for i in company_list:
    if i.total < avg_profit:
        print(f'У компании {i.name} прибыль ниже средней прибыли компаний')
