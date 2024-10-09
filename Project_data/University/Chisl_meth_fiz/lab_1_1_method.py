def equation(x):
    return 3*x**4 + 8*x**3 + 6*x**2 - 10

def dichotomy_method(a, b, eps):
    if equation(a)*equation(b) >= 0:
        print("Указан неправильный интервал")
        return None

    c = a
    while ((b-a) >= eps):
        c = (a+b)/2

        if (equation(c) == 0.0):
            break

        if (equation(c)*equation(a) < 0):
            b = c
        else:
            a = c

    return c

# Интервал [a, b]
a = -3
b = -1

# Точность
eps = 1e-6

print("Корень уравнения:", dichotomy_method(a, b, eps))