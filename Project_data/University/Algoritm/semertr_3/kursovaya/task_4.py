import numpy as np
from scipy import integrate 

# Определяем функции
def f1(x):
    return x / (x**2 + 6*x + 1)

def f2(x):
    return (10**(0.01*x)) * np.cos(0.125*x)

def f3(x):
    return np.arccos((3*x + 25) / 100)

# Функция для вычисления интеграла методом Симпсона
def compute_integral(func, a, b):
    result, error = integrate.quad(func, a, b)
    return result

lower_base = int(input('Введите нижнее основание интеграла: '))
upper_base = int(input('Введите верхнее основание интеграла: '))

# Используем функции
print("Интеграл f1 от 0 до 1: ", compute_integral(f1, lower_base, upper_base))
print("Интеграл f2 от 0 до 1: ", compute_integral(f2, lower_base, upper_base))
print("Интеграл f3 от 0 до 1: ", compute_integral(f3, lower_base, upper_base))