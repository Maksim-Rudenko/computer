'''Сформировать массив из элементов исходных массивов, непринадлежащих промежутку [-4;6], и из элементов, 
больших 12, второго массива.'''


# Ввод размера массивов и его элементов
mas_1_len = int(input('Введите длину первого массива: '))
mas_1 = []
for i in range(mas_1_len):
    val = float(input('Введите элемент массива: '))
    mas_1.append(val)

mas_2_len = int(input('Введите длину второго массива: '))
mas_2 = []
for i in range(mas_2_len):
    val = float(input('Введите элемент массива: '))
    mas_2.append(val)

mas_result = []

for i in range(len(mas_1)):
    if mas_1[i] < -4 or mas_1[i] > 6:
        mas_result.append(mas_1[i])

for i in range(len(mas_2)):
    if mas_2[i] < -4 or mas_2[i] > 6:
        mas_result.append(mas_2[i])