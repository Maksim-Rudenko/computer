from math import cos, sin, pi, e, log


x = float(input('Введите значение x: '))

y = pow(cos(pow(e, x)) + log(pow(1 + x, 2)) + pow((pow(e, cos(x)) + pow(sin(pi * x), 2)), 0.5) + pow(x, -0.5) + cos(pow(x, 2)), sin(x))

print('Результат значения выражения:', y)