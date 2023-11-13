import pandas as pd

# 1 Создать список и вывести его в развенутом виде

lst = [1, 2, 3]
lst.reverse() # 1 method
print(lst)
print(lst[::-1]) # 2 method


# 2 Ф-ция берет на вход 3 значения: сумма вклада, процент, кол-во лет. Калькулятор вклада сделать
def func(income, percent, years):
    '''Формула сложного процента'''
    return income * (1 + percent / 100) ** years
print(func(1000, 5, 10))


# 3 DataFrame из 2 столбцов: месяц, продажи
inf = {'month': [1, 2, 3, 4, 5], 'cells': [10, 53, 45, 23, 58]}
df = pd.DataFrame(inf)
# Добавить 2 столбца: 1 - сумма продаж за этот месяц + предыдущие
#                     2 - сравнивание роста продаж по отношению к прошлому месяцу

df['sum_cells'] = [0 for i in range(len(df['cells']))]
for i in range(len(df['cells'])):
    if i == 0:
        df['sum_cells'][i] = df['cells'][i]
    else:
        df['sum_cells'][i] = df['sum_cells'][i - 1] + df['cells'][i]
# А можно использовать функцию: df['sum_cells'] = df['cells'].cumsum()

df['raz_cells'] = [0.0 for i in range(len(df['cells']))]
for i in range(1, len(df['cells'])):
    df['raz_cells'][i] = (df['cells'][i] - df['cells'][i - 1]) / df['cells'][i - 1] * 100
# df['raz_cells'] = (df.cells - df.cells.shift()) / df.cells
print(df)