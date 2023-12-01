from math import log, sin


x_start = float(input('Введите начальное значение x: '))
x_finish = float(input('Введите начальное значение x: '))
x_step = float(input('Введите дельта x: '))

n = int((x_finish - x_start) / x_step) + 1
x = x_start

print('for loop:')
for i in range(n):
    if x < 0:
        y = log(x ** 2 + 1) + 2 * x
    elif x >= 0 and x < 2:
        y = sin(2 * x) ** 2
    else:
        y = pow(x ** 2 + x + 1, 0.5)

    print('x: {} y: {}'.format(x, y))
    x += x_step

x = x_start
print('while loop:')
while x <= x_finish:
    if x < 0:
        y = log(x ** 2 + 1) + 2 * x
    elif x >= 0 and x < 2:
        y = sin(2 * x) ** 2
    else:
        y = pow(x ** 2 + x + 1, 0.5)

    print('x: {} y: {}'.format(x, y))
    x += x_step

