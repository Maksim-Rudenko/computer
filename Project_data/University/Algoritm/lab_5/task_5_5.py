#  Дано натуральное k. Определить k-ю цифру последовательности: 
#1525125625..., в которой выписаны подряд степени 5.

k = int(input("Введите число k: "))

sequence = ''
degree = 0

while len(sequence) < k:
    sequence += str(pow(5, degree))
    degree += 1

print(sequence)
print(sequence[k - 1])

