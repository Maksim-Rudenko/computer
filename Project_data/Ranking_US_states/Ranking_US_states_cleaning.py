# Данный код сделан для поверхностной очистки данных для представления в Tableu

import pandas as pd

df = pd.read_csv('Ranking of United States cities by area.csv')

# Так как анализ площадей буду производить на основании кв. километров, то значения в милях удаляем
df.drop(labels=['Land area (sq mi)', 'Water area (sq mi)', 'Total area (sq mi)'], axis=1, inplace=True)

# Для удобства переименовываем названия категорий (столбцов)
df = df.rename(columns={'City ': 'City', 'State ': 'State', ' (km2)': 'Land area, km2',
                        ' (km2).1': 'Water area, km2', ' (km2).2': 'Total area, km2'})

# Убираем ',' чтобы не мешали
df['Land area, km2'] = df['Land area, km2'].apply(lambda x: x.replace(',', ''))
df['Water area, km2'] = df['Water area, km2'].apply(lambda x: x.replace(',', ''))
df['Total area, km2'] = df['Total area, km2'].apply(lambda x: x.replace(',', ''))
df['Population (2020)'] = df['Population (2020)'].apply(lambda x: x.replace(',', ''))

# Изменяем тип данных числовых критериев
df['Land area, km2'] = df['Land area, km2'].astype('float64')
df['Water area, km2'] = df['Water area, km2'].astype('float64')
df['Total area, km2'] = df['Total area, km2'].astype('float64')
df['Population (2020)'] = df['Population (2020)'].astype('int64')

df.to_csv('Ranking_US_states_after_cleaning.csv', index=False)
