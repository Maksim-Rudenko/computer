x = float(input('Введите значение x: '))
eps = float(input('Введите значение точности: '))

a1 = x / 3 # значение первого элемента последовательности


def func(a_pred, i):
    '''Расчет следующего элемента последовательности на основании 
    предыдущего и номера элемента в последовательности'''
    a_posled = a_pred * (-(x * i * (i + 2)) / ((i + 1) * (i + 3)))
    
    return a_posled

i = 1
a2 = func(a1, i) # расчет второго элемента последовательности

a_first, a_second = a1, a2
s = a_first # сумма ряда из одного первого элемента

while abs(a_second - a_first) > eps:
    s += a_second # увеличиваем значение суммы ряда на значение последующего элемента
    a = a_first
    i += 1
    a_first = a_second
    a_second = func(a_first, i) # расчитан последующий элемент

print(s)