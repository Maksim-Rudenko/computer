#Заданы три натуральных числа А, В и N. Найти все натуральные числа, 
#не превосходящие N, которые можно представить в виде суммы 
#(произвольного числа) слагаемых, каждое из которых — А или В.

a = int(input('Введите значение A: '))
b = int(input('Введите значение B: '))
n = int(input('Введите значение N: '))

if a < b:
   a, b = b, a

res = [a]

for c in range(1, n):
   for x in range(int(n/a) + 1):
      y = (c - a * x) / b      
      if int(y) == y and (y * b + a * x) <= n and y > 0:
         res.append(int(y * b + a * x))

print(set(res))

