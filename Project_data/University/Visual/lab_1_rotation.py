import numpy as np
import math
import matplotlib.pyplot as plt

plus_x = 0
plus_y = 0

# Масщтабирование по осям
x_size = 1
y_size = 1

'''# house_2
x = (np.array([10, 10, 20, 30, 30, 10]) + plus_x) * x_size
y = (np.array([10, 20, 27, 20, 10, 10]) + plus_y) * y_size

# window_2
x1 = (np.array([15, 15, 25, 25, 15]) + plus_x) * x_size
y1 = (np.array([12, 18, 18, 12, 12]) + plus_y) * y_size'''

#var_9
# внешняя
x = (np.array([10, 35, 25, 20, 10]) + plus_x) * x_size
y = (np.array([5, 5, 30, 30, 5]) + plus_y) * y_size

# внутренняя
x1 = (np.array([20, 25, 25, 20, 20]) + plus_x) * x_size
y1 = (np.array([10, 10, 20, 20, 10]) + plus_y) * y_size


# расстояния от начала координат до каждой точки рисунка
r = [pow(x[i]**2 + y[i]**2, 0.5) for i in range(len(x))]
r1 = [pow(x1[i]**2 + y1[i]**2, 0.5) for i in range(len(x1))]

# углы beta при векторе, образующимся при проведении прямой от начала координат до точки рисунка
beta_r = [math.asin(y[i] / r[i]) for i in range(len(r))]   #радианы
beta_r1 = [math.asin(y1[i] / r1[i]) for i in range(len(r1))]   #радианы

# угол поворота в радианах
alpha = 0

# новые координаты точек с учетом поворота на угол alpha
new_x = [r[i] * math.cos(beta_r[i] + alpha) for i in range(len(r))]
new_y = [r[i] * math.sin(beta_r[i] + alpha) for i in range(len(r))]
new_x1 = [r1[i] * math.cos(beta_r1[i] + alpha) for i in range(len(r1))]
new_y1 = [r1[i] * math.sin(beta_r1[i] + alpha) for i in range(len(r1))]

# Закрепил значения по осям, чтобы было видно наглядно смещение
plt_max = max(max(x), max(y)) * 1.5
plt.ylim(-30, plt_max)
plt.xlim(-30, plt_max)

plt.plot(new_x, new_y, color='black')
plt.plot(new_x1, new_y1, color='black')

plt.title("House")

plt.show()