# Данный код сделан для поверхностной очистки данных для представления в Tableu

import pandas as pd
from sklearn.impute import SimpleImputer

coffe_df = pd.read_csv('df_arabica_clean.csv')

# print(coffe_df.info())

# Удаляем ненужные категории (Unnamed: 0, ID)
# В категории ICo Number много пропущенных значений, поэтому тоже удаляем
coffe_df.drop(labels=['Unnamed: 0', 'ID', 'ICO Number'], axis=1, inplace=True)

# Заменим пропущенные категориальные признаки наиболее часто встречающимися значениями

imputer = SimpleImputer(strategy="most_frequent")
val_list = coffe_df.select_dtypes(include=["object"]).columns.tolist()
coffe_df[val_list] = imputer.fit_transform(coffe_df[val_list])


# Заменим тип данных в некоторых категориях
coffe_df['Bag Weight'] = coffe_df['Bag Weight'].str.split().str.get(0).astype(int)
coffe_df['Harvest Year'] = coffe_df['Harvest Year'].str.split('/').str.get(0).astype(int)
coffe_df['Grading Date'] = coffe_df['Grading Date'].str.split(',').str.get(1).astype(int) # берем год
coffe_df['Expiration'] = coffe_df['Expiration'].str.split(',').str.get(1).astype(int) # берем год

print(coffe_df.info())

coffe_df.to_csv('Coffe_data_after_cleaning.csv', index=False)