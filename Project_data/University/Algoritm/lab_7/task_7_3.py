'''Сформировать массив из элементов исходных массивов, непринадлежащих промежутку [-4;6], и из элементов, 
больших 12, второго массива.'''


# Ввод размера массивов и его элементов
mas_1_len = int(input('Введите длину первого массива: '))
mas_1 = []
for i in range(mas_1_len):
    val = float(input('Введите элемент первого массива: '))
    mas_1.append(val)

mas_2_len = int(input('Введите длину второго массива: '))
mas_2 = []
for i in range(mas_2_len):
    val = float(input('Введите элемент второго массива: '))
    mas_2.append(val)

mas_result = []

# заполняем массив числами непринадлежащих промежутку [-4;6] первого исходного массива
for i in range(len(mas_1)):
    if mas_1[i] < -4 or mas_1[i] > 6:
        mas_result.append(mas_1[i])

# заполняем массив числами больших 12 второго исходного массива
for i in range(len(mas_2)):
    if mas_2[i] > 12:
        mas_result.append(mas_2[i])

print("Исходные массивы:\n{}\n{}".format(mas_1, mas_2))
if len(mas_result) > 0:
    print("Результат:\n{}".format(mas_result))
else:
    print("Массив не был сформирован")



'''
#include <stdio.h>

int main() {
    int mas_1_len;
    printf("Введите длину первого массива: ");
    scanf("%d", &mas_1_len);
    float mas_1[mas_1_len];
    for (int i = 0; i < mas_1_len; i++) {
        printf("Введите элемент первого массива: ");
        scanf("%f", &mas_1[i]);
    }
    int mas_2_len;
    printf("Введите длину второго массива: ");
    scanf("%d", &mas_2_len);
    float mas_2[mas_2_len];
    for (int i = 0; i < mas_2_len; i++) {
        printf("Введите элемент второго массива: ");
        scanf("%f", &mas_2[i]);
    }
    float mas_result[mas_1_len + mas_2_len];
    int result_index = 0;
    for (int i = 0; i < mas_1_len; i++) {
        if (mas_1[i] < -4 || mas_1[i] > 6) {
            mas_result[result_index] = mas_1[i];
            result_index++;
        }
    }
    for (int i = 0; i < mas_2_len; i++) {
        if (mas_2[i] > 12) {
            mas_result[result_index] = mas_2[i];
            result_index++;
        }
    }
    printf("Исходные массивы:\n");
    for (int i = 0; i < mas_1_len; i++) {
        printf("%f ", mas_1[i]);
    }
    printf("\n");
    for (int i = 0; i < mas_2_len; i++) {
        printf("%f ", mas_2[i]);
    }
    printf("\n");
    if (sizeof(mas_result) / sizeof(mas_result[0]) > 0) {
        printf("Результат:\n");
    for (int i = 0; i < result_index; i++) {
        printf("%f ", mas_result[i]);
    }
    } else {
        printf("Массив не был сформирован");
    }
    return 0;
}
'''