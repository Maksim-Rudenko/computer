from math import pi, tan


a = float(input('Введите значение первого основания трапеции: '))
b = float(input('Введите значение второго основания трапеции: '))

if a == b:
    print('Такой трапеции не существует')
    exit()
if a > b:
    a, b = b, a


alpha = float(input('Введите значение угла при больщем основании трапеции: '))
alpha_rad = alpha * (pi / 180)

h = ((b - a) / 2) * tan(alpha_rad)
s = ((b + a) / 2) * h

print('Высота трапеции: ', h)
print('Площадь трапеции: ', s)
