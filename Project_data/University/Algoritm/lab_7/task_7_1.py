'''Вычислить сумму квадратов чисел, принадлежащих промежутку [X, Y) и количество
отрицательных чисел, стоящих на четных местах'''

# Ввод размера массива и его элементов
mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

# Ввод размера промежутка [X, Y)
x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))

result_sum = 0
result_count = 0

for i in range(0, len(mas)):
    if mas[i] >= x and mas[i] < y:
        result_sum += pow(mas[i], 2)
    if i % 2 != 0 and mas[i] < 0:
        result_count += 1

print('Исходный массив: {}\nИнтервал [X, Y): [{}, {})'.format(mas, x, y))
print('Сумма квадратов чисел, принадлежащих промежутку [X, Y): {}'.format(result_sum))
print('Количество отрицательных чисел, стоящих на четных местах: {}'.format(result_count))
      