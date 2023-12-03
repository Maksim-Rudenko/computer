#Заданы три натуральных числа А, В и N. Найти все натуральные числа, 
#не превосходящие N, которые можно представить в виде суммы 
#(произвольного числа) слагаемых, каждое из которых — А или В.

a = int(input('Введите значение A: '))
b = int(input('Введите значение B: '))
n = int(input('Введите значение N: '))

res = []
if a > n and b > n:
   print('Невозможно решить, значение N слишком маленькое')
   exit()
elif a > n and b <= n:
   res = [b]
elif a <= n and b > n:
   res = [a]
else:
   res = [b, a]

temp1 = 0
temp2 = 0
i = 0
while i < len(res):
   temp1 = res[i] + b
   temp2 = res[i] + a 
   if temp1 not in res and temp1 < n:
      res.append(temp1)
   if temp2 not in res and temp2 < n:
      res.append(temp2)
   i += 1
print(res)  


'''
Альтернативное решение
if a < b:
   a, b = b, a
for c in range(1, n):
   for x in range(int(n/a) + 1):
      y = (c - a * x) / b      
      if int(y) == y and (y * b + a * x) <= n and y > 0:
         res.append(int(y * b + a * x))

print(set(res))'''


'''
#include <stdio.h>

int main() {
    int a, b, n;
    printf("Введите значение A: ");
    scanf("%d", &a);
    printf("Введите значение B: ");
    scanf("%d", &b);
    printf("Введите значение N: ");
    scanf("%d", &n);
    int res[100];
    int resSize = 0;

    if (a > n && b > n) {
        printf("Невозможно решить, значение N слишком маленькое\n");
        return 0;
    } else if (a > n && b <= n) {
        res[resSize++] = b;
    } else if (a <= n && b > n) {
        res[resSize++] = a;
    } else {
        res[resSize++] = b;
        res[resSize++] = a;
    }

    int temp1, temp2;
    int i = 0;
    while (i < resSize) {
        temp1 = res[i] + b;
        temp2 = res[i] + a;
        if (temp1 < n) {
            int found = 0;
            for (int j = 0; j < resSize; j++) {
                if (res[j] == temp1) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                res[resSize++] = temp1;
            }
        }
        if (temp2 < n) {
            int found = 0;
            for (int j = 0; j < resSize; j++) {
                if (res[j] == temp2) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                res[resSize++] = temp2;
            }
        }
        i++;
    }

    for (int i = 0; i < resSize; i++) {
        printf("%d ", res[i]);
    }
    printf("\n");

    return 0;
}
'''