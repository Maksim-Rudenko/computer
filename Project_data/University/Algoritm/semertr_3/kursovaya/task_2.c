#include <stdio.h>
#include <math.h> 

// Функция для подсчета отрицательных чисел на четных позициях
int count_negatives(int arr[], int size) {
    int count = 0;
    if (size == 0) {
        return count;
    }
    // Считаем, что элемент с индексом 0 - нечетный
    for (int i = 1; i < size; i += 2) {
        if (arr[i] < 0) {
            count++;
        }
    }
    return count;
}

int main() {
    int T[100], P[100], Q[100];
    int size_T, size_P, size_Q;
    double L;

    // Ввод размеров массивов
    printf("Введите размер массива T: ");
    scanf("%d", &size_T);
    printf("Введите размер массива P: ");
    scanf("%d", &size_P);
    printf("Введите размер массива Q: ");
    scanf("%d", &size_Q);

    // Ввод элементов массивов
    if (size_T > 0) {
        printf("Введите элементы массива T через Enter: ");
        for (int i = 0; i < size_T; i++) {
            scanf("%d", &T[i]);
        }
    }
    if (size_P > 0) {
        printf("Введите элементы массива P через Enter: ");
        for (int i = 0; i < size_P; i++) {
            scanf("%d", &P[i]);
        }
    }
    if (size_Q > 0) {
        printf("Введите элементы массива Q через Enter: ");
        for (int i = 0; i < size_Q; i++) {
            scanf("%d", &Q[i]);
        }
    }

    // Подсчет отрицательных чисел на четных позициях
    int a = count_negatives(T, size_T);
    int b = count_negatives(P, size_P);
    int c = count_negatives(Q, size_Q);
    
    // Расчет функции L    
    L = 2.3 * sin(a) - pow(cos(b), 2) + 3.3 * c;
    printf("L = %lf\n", L);
    return 0;
}