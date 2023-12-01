from math import atan

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
x_start = float(input('Введите начальное значение x: '))
x_finish = float(input('Введите начальное значение x: '))
num_inter = int(input('Введите число интервалов значения x: '))

x_step = (x_finish - x_start) / num_inter

result = {}

while x_start < x_finish:
    y = atan(a + x_start) / pow(a ** 3 + b ** 3, 0.5)    
    print('x: {} y: {}'.format(x_start, y))
    x_start += x_step



