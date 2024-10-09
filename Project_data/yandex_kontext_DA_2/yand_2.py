import numpy as np
import itertools

def value(n, a):
    mat_value = dict()
    # расчет мат ожидания для количества выпадния решки в зависимости от количества монет
    for i in range(n + 1):
        mat_value[i] = np.mean([j for j in range(i + 1)])
    mat_value[0] = 0

    # комбиации остатка монет
    combinations = [seq for i in range(len(a), 0, -1) for seq in itertools.combinations(a, i)]

    # расчет денег на основании остатка монет и мат ожиданния (степени тройки) выпадения решки
    result = dict()
    for i in range(len(combinations)):
        result[combinations[i]] = sum(combinations[i]) + 3 ** (mat_value[n - len(combinations[i])])
    result[0] = 3 ** mat_value[n]

    # нахождение наиболее выгодного вариата
    max_val = max(result.values())
    final_dict = {worker:value for worker, value in result.items() if value == max_val}
    for key in final_dict.keys():
        return len(key)
    
n = int(input())

input_array = input()
a = [int(x) for x in input_array.split()]

print(value(n, a))

