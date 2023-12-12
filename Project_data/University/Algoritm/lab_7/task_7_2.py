'''Найти минимальный элемент и вместо него записать N^2'''
# Вывести исходный массив, мин  эл-т и его номер, результат


# Ввод размера массива и его элементов
mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

check_val = mas[0]
check_index = 0

# Нахождение минимального элемента через цикл
for i in range(len(mas)):
    if mas[i] < check_val:
        check_val = mas[i]
        check_index = i

# Замена минимального элемента массива на его квадрат
mas_result = mas.copy()
mas_result[check_index] = pow(check_val, 2)

print('Исходный массив: {}'.format(mas))
print('Минимальный элемент массива: {}'.format(check_val))
print('Номер минимального элемента массива: {}'.format(check_index + 1))
print('Результат: {}'.format(mas_result))