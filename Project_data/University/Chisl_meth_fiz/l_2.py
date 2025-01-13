import numpy as np

# Матрица коэффициентов и вектор правой части
A = np.array([
    [1, 3, 2],
    [1, 2, 3],
    [3, 1, 2]
], dtype=float)

b = np.array([1, 6, 7], dtype=float)

# Метод Гаусса с частичным выбором главного элемента
def gauss_method(A, b):
    n = len(b)
    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

# Метод LU-разложения (с частичным выбором главного элемента)
def lu_decomposition(A, b):
    n = len(b)
    L = np.zeros((n, n))
    U = A.copy()
    for i in range(n):
        max_row = np.argmax(abs(U[i:, i])) + i
        U[[i, max_row]] = U[[max_row, i]]
        L[[i, max_row], :i] = L[[max_row, i], :i]
        b[i], b[max_row] = b[max_row], b[i]

        L[i, i] = 1
        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] -= L[j, i] * U[i, i:]

    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x

# Метод прогонки (Трехдиагональная матрица)
def tridiagonal_solver(A, b):
    n = len(b)
    a = np.zeros(n - 1)  # Поддиагональные элементы
    b_main = np.zeros(n)  # Диагональные элементы
    c = np.zeros(n - 1)  # Наддиагональные элементы
    d = b.copy()  # Копируем вектор правых частей

    # Заполнение массивов a, b_main и c
    for i in range(n - 1):
        a[i] = A[i + 1, i]
        c[i] = A[i, i + 1]
    b_main[:] = np.diag(A)

    # Прямой ход
    for i in range(1, n):
        factor = a[i - 1] / b_main[i - 1]
        b_main[i] -= factor * c[i - 1]
        d[i] -= factor * d[i - 1]

    # Обратный ход
    x = np.zeros(n)
    x[-1] = d[-1] / b_main[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b_main[i]

    return x

# Метод простой итерации
def simple_iteration(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.ones(n)  # Начальное приближение
    D = np.diag(A)
    R = A - np.diagflat(D)

    for _ in range(max_iter):
        D_safe = np.where(D == 0, 1e-10, D)  # Избегаем деления на ноль
        x_new = (b - np.dot(R, x)) / D_safe
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new

    return x

# Метод Гаусса-Зейделя
def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.ones(n)  # Начальное приближение

    for _ in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            denominator = A[i, i] if A[i, i] != 0 else 1e-10  # Избегаем деления на ноль
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / denominator
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new

    return x

# Проверка, является ли матрица трехдиагональной
def is_tridiagonal(A):
    n = A.shape[0]
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and A[i, j] != 0:
                return False
    return True

# Проверка, является ли матрица диагонально преобладающей
def is_diagonally_dominant(A):
    for i in range(len(A)):
        sum_row = sum(abs(A[i][j]) for j in range(len(A)) if i != j)
        if abs(A[i][i]) <= sum_row:
            return False
    return True

print("Матрица A:")
print(A)

if is_tridiagonal(A):
    print("Матрица A подходит для метода прогонки (трехдиагональная).")
    try:
        solution_tridiagonal = tridiagonal_solver(A.copy(), b.copy())
    except Exception as e:
        solution_tridiagonal = f"Ошибка: {e}"
else:
    print("Матрица A не подходит для метода прогонки.")
    solution_tridiagonal = "Матрица не является трехдиагональной" 

if is_diagonally_dominant(A):
    solution_iteration = simple_iteration(A.copy(), b.copy())
    solution_gauss_seidel = gauss_seidel(A.copy(), b.copy())
else:
    solution_iteration = solution_gauss_seidel = "Не сходится"
    print("Матрица A не удовлетворяет условию диагонального преобладания.")

solution_gauss = gauss_method(A.copy(), b.copy())
solution_lu = lu_decomposition(A.copy(), b.copy())
solution_numpy = np.linalg.solve(A, b)

print("Решение методом Гаусса:", solution_gauss)
print("Решение методом LU-разложения:", solution_lu)
print("Решение методом прогонки:", solution_tridiagonal)
print("Решение методом простой итерации:", solution_iteration)
print("Решение методом Гаусса-Зейделя:", solution_gauss_seidel)
print("Решение встроенной функцией numpy.linalg.solve:", solution_numpy)
