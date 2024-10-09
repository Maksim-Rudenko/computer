import matplotlib.pyplot as plt

#x = [int(i) for i in range(-10, 10)]

x = [(i / 100) for i in range(-250, -200)]

y = [0 for i in range(len(x))]

for i in range(len(x)):
    y[i] = 3 * pow(x[i], 4) + 8 * pow(x[i], 3) + 6 * pow(x[i], 2) - 10
print('x: ', x)
print('y: ', y)

plt.plot(x, y)
plt.axis([-1, -3, 0, 10])
plt.show()