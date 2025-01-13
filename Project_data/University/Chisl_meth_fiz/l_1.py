import math
import matplotlib.pyplot as plt
import numpy as np

# Функция, для которой ищем корень
def func(x):
    try:        
        return pow(x, 4) - pow(x, 3) - 2 * pow(x, 2) + 3 * x - 3
    except ValueError:
        return float('nan')

# Производная функции для метода Ньютона
def dfunc(x):
    try:        
        result = 4 * pow(x, 3) - 3 * pow(x, 2) - 4 * x + 3
        if isinstance(result, complex):
            return float('nan')
        return result
    except (ValueError, TypeError):
        return float('nan')

# Метод половинного деления (дихотомии)
def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Функция имеет одинаковые знаки на концах отрезка.")
        return None
    c = (a + b) / 2.0  # Начальное значение
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

# Метод хорд (пропорциональных частей)
def secant_method(f, a, b, tol):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    c = b
    while abs(b - a) > tol:
        try:
            c = b - f(b) * (b - a) / (f(b) - f(a))
        except ZeroDivisionError:
            return b
        a, b = b, c
    return c

# Метод касательных (метод Ньютона)
def newton_method(f, df, x0, tol):
    x = x0
    while abs(f(x)) > tol:
        try:
            x_new = x - f(x) / df(x)
            if isinstance(x_new, complex):
                return float('nan')
            x = x_new
        except ZeroDivisionError:
            return x
    return x

# Метод простой итерации (последовательных приближений)
def fixed_point_iteration(g, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        try:
            x_new = g(x)
            if isinstance(x_new, complex):
                return float('nan')
        except (ValueError, TypeError, OverflowError):
            return x
        if abs(x - x_new) < tol:
            return x_new
        x = x_new
    return None

# Функция для построения графиков
def plot_function_and_root(f, root, method_name):
    x = np.linspace(-2, -1, 400)  # Диапазон [-2, -1], чтобы избежать отрицательных значений
    y = [f(i) for i in x]

    plt.figure()
    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(root, color='red', linestyle='--', label=f'Корень ({method_name})')
    plt.scatter(root, f(root), color='red')
    plt.title(f'График функции и корень ({method_name})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Пример использования методов
def main():
    print("Метод половинного деления:")
    root = bisection_method(func, -2, -1, 0.0001)  # Диапазон [-2, -1]
    print(f"Корень: {root}\n")
    plot_function_and_root(func, root, "Метод половинного деления:")

    print("Метод хорд:")
    root = secant_method(func, -2, -1, 0.0001)  # Диапазон [-2, -1]
    print(f"Корень: {root}\n")
    plot_function_and_root(func, root, "Метод хорд")

    print("Метод касательных (метод Ньютона):")
    root = newton_method(func, dfunc, -2, 0.0001)  # Начальное значение -2
    print(f"Корень: {root}\n")
    plot_function_and_root(func, root, "Метод касательных")

    print("Метод простой итерации:")
    def g(x):     
            return (pow(x, 3) + 2 * pow(x, 2) - pow(x, 4) + 3) / 3                    
    root = fixed_point_iteration(g, -2, 0.0001, 100)  # Начальное значение -2
    print(f"Корень: {root}")
    plot_function_and_root(func, root, "Метод простой итерации")

if __name__ == "__main__":
    main()
