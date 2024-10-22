#include <stdio.h>

// Функция умножения элементов матрицы на 5
void multiply_by_five(int rows, int cols, int source[rows][cols], int result[rows][cols]) {
    for (int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            result[i][j] = 5 * source[i][j];
        }
    }
}

int main() {
    int rows, cols;

    // Ввод размера матриц (количество строк и столбцов)
    printf("Введите количество строк матрицы: ");
    scanf("%d", &rows);
    printf("Введите количество столбцов матрицы: ");
    scanf("%d", &cols);

    int A[rows][cols];
    int B[rows][cols];

    // Ввод эмементов матриц
    printf("Введите элементы матрицы A:\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Введите элементы матрицы B:\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    // Вывод исходных матриц A И B
    printf("Матрица A:\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    printf("Матрица B:\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
    int P[rows][cols];
    int Q[rows][cols];

    // Формирование матриц P И Q на основании матриц A И B
    multiply_by_five(rows, cols, A, P);
    multiply_by_five(rows, cols, B, Q);

    // Вывод матриц P И Q
    printf("Матрица P:\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            printf("%d ", P[i][j]);
        }
        printf("\n");
    }
    printf("Матрица Q:");
    printf("\n");
    for (int i=0; i<rows; i++) {
        for (int j=0; j<cols; j++) {
            printf("%d ", Q[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}