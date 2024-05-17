'''
Отсортировать массив по невозрастанию методом извлечения 
минимального элемента, поиск минимального элемента 
проводить справа налево.

#include <stdio.h>

int main() {
    int mas[10];
    int n, i, j, k, imax, x;
    
    printf("Введите количество элементовв массиве:");
    scanf("%d", &n);
    
    printf("Исходный массив\n");
    for (i = 0; i < n; i++) {
        //printf("a[%d]=", i+1);
        scanf("%d", &mas[i]);
    }
    
    printf("\n");
    
    for (i = 0; i < n-1; i++) {
        imax = 0;
        for (j = 1; j < n-i; j++) {
            if (mas[j] < mas[imax]) {
                imax = j;
            }
        }
        x = mas[imax];
        for (j = imax; j < n-i; j++) {
            mas[j] = mas[j+1];
        }
        mas[n-i-1] = x;
    }
    
    printf("Отсортированный массив\n");
    for (i = 0; i < n; i++) {
        printf("%4d", mas[i]);
    }
    
    return 0;
}
'''