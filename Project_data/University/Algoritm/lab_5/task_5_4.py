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