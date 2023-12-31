'''Сформировать массив из отрицательных элементов исходного 
массива, расположенных после третьего нуля, и найти в нем 
максимальное и минимальное значения.'''


mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

null_check = 0
new_mas = []

min_val = 0
max_val = float('-inf')

for i in range(mas_len):
    if mas[i] == 0:
        null_check += 1
    if null_check >= 3 and mas[i] < 0:
        new_mas.append(mas[i])
        if max_val < mas[i]:
            max_val = mas[i]
        if min_val > mas[i]:
            min_val = mas[i]
            

print("Результат:\n{}".format(new_mas))
print("максимальное и минимальное значения массива: {} и {} соответственно".format(max_val, min_val))



# В С массив определенного размера и задается этот размер изначально. Поэтому там вместо некоторых
# элементов, что не вошли в массив будут null (условно)
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
    
    int null_check = 0;
    float new_mas[mas_len];
    float min_val = 0;
    float max_val = -INFINITY;
    
    for (int i = 0; i < mas_len; i++) {
        if (mas[i] == 0) {
            null_check += 1;
        }
        if (null_check >= 3 && mas[i] < 0) {
            new_mas[i] = mas[i];
            if (max_val < mas[i]) {
                max_val = mas[i];
            }
            if (min_val > mas[i]) {
                min_val = mas[i];
            }
        }
    }
    
    printf("Результат:\n");
    for (int i = 0; i < mas_len; i++) {
        if (new_mas[i] != 0) {
            printf("%f ", new_mas[i]);
        }
    }
    printf("\n");
    
    printf("максимальное и минимальное значения массива: %f и %f соответственно\n", max_val, min_val);
    
    return 0;
}
'''