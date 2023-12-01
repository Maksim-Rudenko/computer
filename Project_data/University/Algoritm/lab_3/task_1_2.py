from math import cos


x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))
z = float(input('Введите значение z: '))

def function(x, y, z):
    return x + (((z * y) ** (1/3)) / (y + cos(x)))
 
print(function(x, y, z))