def equation(x):
    return 3*x**4 + 8*x**3 + 6*x**2 - 10

def chord_method(a, b, eps):
    x0, x1 = a, b
    while abs(x1 - x0) > eps:
        x0, x1 = x1, x1 - (x1 - x0) / (equation(x1) - equation(x0)) * equation(x1)
    return x1

# Интервал [a, b]
a = -3
b = -1

# Точность
eps = 1e-6

print("Корень уравнения:", chord_method(a, b, eps))