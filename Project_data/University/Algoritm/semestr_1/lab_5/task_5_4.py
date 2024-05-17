#Выполнить следующие задания, используя алгоритмы для 
#нахождения делителей числа

#Вычислить НОД натуральных чисел а,b.

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

temp = min(a, b)
for i in range(1, temp + 1): 
    if(( a % i == 0) and (b % i == 0 )): 
        gcd = i

print("НОД чисел a и b:", gcd) 


'''
#include <stdio.h>

int main() {
    int a, b;
    printf("Введите число a: ");
    scanf("%d", &a);
    printf("Введите число b: ");
    scanf("%d", &b);

    int temp = (a < b) ? a : b;
    int gcd;
    for (int i = 1; i <= temp; i++) {
        if ((a % i == 0) && (b % i == 0)) {
            gcd = i;
        }
    }

    printf("НОД чисел a и b: %d", gcd);

    return 0;
}
'''


# Дано натуральное n. Получить все простые делители этого числа.

n = int(input("Введите число n: "))

print("Простые делители:", end = " ")
for i in range(n - 1, 1, -1):
    is_simple = 0
    if n % i == 0:
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                is_simple += 1
        if is_simple == 0:
            print(i, end = " ")

'''
#include <stdio.h>

int main() {
    int n;
    printf("Введите число n: ");
    scanf("%d", &n);

    printf("Простые делители: ");
    for (int i = n - 1; i > 1; i--) {
        int is_simple = 0;
        if (n % i == 0) {
            for (int j = i - 1; j > 1; j--) {
                if (i % j == 0) {
                    is_simple++;
                }
            }
            if (is_simple == 0) {
                printf("%d ", i);
            }
        }
    }

    return 0;
}
'''