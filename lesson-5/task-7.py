"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

if __name__ == '__main__':
    average_revenue = []
    pure_revenue = []
    firms = []
    average_profit = {}
    final_result = []

    with open('../lesson-5/task-7.txt', 'r') as f:
        for line in f:
            firm, type_of_ownership, revenue, costs = line.split()
            firms.append(firm)
            pure_revenue.append(int(revenue) - int(costs))
            if int(costs) < int(revenue):
                average_revenue.append(int(revenue))

        average_profit['average_profit'] = (sum(average_revenue)) / len(average_revenue)
        firms_dict = {k: v for (k, v) in zip(firms, pure_revenue)}
        print([firms_dict, average_profit])
