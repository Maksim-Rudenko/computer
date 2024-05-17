'''Найти минимальный элемент и вместо него записать N^2'''
# Вывести исходный массив, мин  эл-т и его номер, результат


# Ввод размера массива и его элементов
mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

check_val = mas[0]
check_index = 0

# Нахождение минимального элемента через цикл
for i in range(len(mas)):
    if mas[i] < check_val:
        check_val = mas[i]
        check_index = i

# Замена минимального элемента массива на его квадрат
mas_result = mas.copy()
mas_result[check_index] = pow(check_val, 2)

print('Исходный массив: {}'.format(mas))
print('Минимальный элемент массива: {}'.format(check_val))
print('Номер минимального элемента массива: {}'.format(check_index + 1))
print('Результат: {}'.format(mas_result))


'''
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int mas_len;
    printf("Введите длину массива: ");
    scanf("%d", &mas_len);

    float *mas = (float *)malloc(mas_len * sizeof(float));
    for (int i = 0; i < mas_len; i++) {
        float val;
        printf("Введите элемент массива: ");
        scanf("%f", &val);
        mas[i] = val;
    }

    float check_val = mas[0];
    int check_index = 0;

    for (int i = 0; i < mas_len; i++) {
        if (mas[i] < check_val) {
            check_val = mas[i];
            check_index = i;
        }
    }

    float *mas_result = (float *)malloc(mas_len * sizeof(float));
    for (int i = 0; i < mas_len; i++) {
        mas_result[i] = mas[i];
    }
    mas_result[check_index] = pow(check_val, 2);

    printf("Исходный массив: ");
    for (int i = 0; i < mas_len; i++) {
        printf("%.2f ", mas[i]);
    }
    printf("\n");

    printf("Минимальный элемент массива: %.2f\n", check_val);
    printf("Номер минимального элемента массива: %d\n", check_index + 1);

    printf("Результат: ");
    for (int i = 0; i < mas_len; i++) {
        printf("%.2f ", mas_result[i]);
    }
    printf("\n");

    free(mas);
    free(mas_result);

    return 0;
}
'''