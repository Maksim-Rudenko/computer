'''Вычислить сумму квадратов чисел, принадлежащих промежутку [X, Y) и количество
отрицательных чисел, стоящих на четных местах'''

# Ввод размера массива и его элементов
mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

# Ввод размера промежутка [X, Y)
x = float(input('Введите значение X: '))
y = float(input('Введите значение Y: '))

result_sum = 0
result_count = 0

for i in range(0, len(mas)):
    if mas[i] >= x and mas[i] < y:
        result_sum += pow(mas[i], 2)
    if i % 2 != 0 and mas[i] < 0:
        result_count += 1

print('Исходный массив: {}\nИнтервал [X, Y): [{}, {})'.format(mas, x, y))
print('Сумма квадратов чисел, принадлежащих промежутку [X, Y): {}'.format(result_sum))
print('Количество отрицательных чисел, стоящих на четных местах: {}'.format(result_count))


'''
#include <stdio.h>
#include <math.h>

int main() {
    int mas_len;
    printf("Введите длину массива: ");
    scanf("%d", &mas_len);

    float mas[mas_len];
    for (int i = 0; i < mas_len; i++) {
        printf("Введите элемент массива: ");
        scanf("%f", &mas[i]);
    }

    float x, y;
    printf("Введите значение X: ");
    scanf("%f", &x);
    printf("Введите значение Y: ");
    scanf("%f", &y);

    float result_sum = 0;
    int result_count = 0;
    for (int i = 0; i < mas_len; i++) {
        if (mas[i] >= x && mas[i] < y) {
            result_sum += pow(mas[i], 2);
        }
        if (i % 2 != 0 && mas[i] < 0) {
            result_count += 1;
        }
    }

    printf("Исходный массив: [");
    for (int i = 0; i < mas_len; i++) {
        printf("%.2f", mas[i]);
        if (i != mas_len - 1) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("Интервал [X, Y): [%.2f, %.2f)\n", x, y);
    printf("Сумма квадратов чисел, принадлежащих промежутку [X, Y): %.2f\n", result_sum);
    printf("Количество отрицательных чисел, стоящих на четных местах: %d\n", result_count);

    return 0;
}
'''