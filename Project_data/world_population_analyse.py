import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('world_pop.csv')

#print(data.info())

# Удалим ненужный столбец
data.drop(labels=['Unnamed: 0'], axis=1, inplace=True)

# Переводим все значения в целые числа (ведь не может быть 0.5 человека)
for col in data.columns[1:]:
    data[col] = data[col].astype('Int64')


# Заполняем пропущенные значения в данных
def filling_missing_data(df=data):
    null_data = df[df.isnull().any(axis=1)]

    # Просматриваем в каких ячейках (каких годах) отсутствуют значения численности начеления для каждой стораны
    NaN_years = {country: [] for country in null_data['country'].index}

    for cntry in null_data['country'].index:
        print('\nFor {}:'.format(null_data['country'][cntry]))
        for col in null_data.columns[1:]:
            if pd.isna(null_data[col][cntry]):
                print('{} - {}'.format(col, null_data[col][cntry]))
                NaN_years[cntry].append(col)

    df = df.fillna(0)
    null_data = null_data.fillna(0)

    # Население Eritrea с 2012 по 2020 годы (взято с сайта https://countrymeters.info/ru/Eritrea)
    Eritrea_population = [3232135, 3265907, 3296572, 3327260, 3359780, 3394875, 3433009, 3475139, 3521907]
    Kuwait_population = [1971536, 1841941, 1715490]
    # West_Bank_and_Gaza - "в простонароде" Палестина
    West_Bank_and_Gaza_population = [1058783, 1083148, 1112795, 1144115, 1170708, 1186676, 1188149, 1175282,
                                     1153924, 1134233, 1126501, 1136555, 1164472, 1206091, 1254167, 1301368,
                                     1343820, 1382020, 1417700, 1453214, 1491036, 1532632, 1577765, 1626146,
                                     1677511, 1731900, 1788997, 1849119, 1913245, 1983402]

    # Заполняем пропущенные данные в Dataframe
    i_1 = 0
    i_2 = 0
    i_3 = 0
    for cntry in null_data['country'].index:  # берем строки, где пропущены данные
        for col in df.columns:  # берем колонки в строках, где пропущены данные
            if col in NaN_years[cntry]:
                if cntry == 60:
                    # null_data = null_data.replace({col: 0}, Eritrea_population[i_1])
                    df = df.replace({col: 0}, Eritrea_population[i_1])
                    i_1 += 1
                elif cntry == 105:
                    # null_data = null_data.replace({col: 0}, Kuwait_population[i_2])
                    df = df.replace({col: 0}, Kuwait_population[i_2])
                    i_2 += 1
                else:
                    # null_data = null_data.replace({col: 0}, West_Bank_and_Gaza_population[i_3])
                    df = df.replace({col: 0}, West_Bank_and_Gaza_population[i_3])
                    i_3 += 1

filling_missing_data()

# Суммируем значения, чтобы получить население для мира в целом (данные в конце DataFrame отдельной строкой)
data.loc[len(data.index)] = data.sum()
data = data.replace(data['country'][len(data.index) - 1], 'Total')

# создаем отдельный лист со значениями итого по годам (для удобства)
world_population_by_year = data.loc[len(data.index) - 1].tolist()
del world_population_by_year[0] # здесь удалили 'Total', которое присутствует в списке

x = [i for i in range(len(data.columns) - 1)] # чтобы каждому значению из упоряд. списка соотв. значение и d
plt.plot(x, world_population_by_year)

plt.xlabel("Year")
plt.ylabel("Population")

plt.title("World population by year")

# заменяем х на годы
plt.xticks(x, [year for year in range(1960, 2021)])
plt.locator_params(axis='x', nbins=10) # ограничивает кол-во отображаемых тиков на оси
plt.show()