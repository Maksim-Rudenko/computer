#include <stdio.h>


void multiplyByFive(int rows, int cols, int source[rows][cols], int result[rows][cols]) {
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            result[i][j] = 5 * source[i][j];
        }
    }
}

int main() {
    int rows, cols;

    // Enter numbeer of rows and cols of the matrix
    printf("Введите количество строк матрицы: ");
    scanf("%d", &rows);
    printf("Введите количество столбцов матрицы: ");
    scanf("%d", &cols);

    int A[rows][cols];
    int B[rows][cols];

    // Enter A, B matrix elements
    printf("Введите элементы матрицы A:\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Введите элементы матрицы B:\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    // Print matrix P and Q
    printf("Massiv A:\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }
    printf("Massiv B:\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            printf("%d ", B[i][j]);
        }
        printf("\n");
    }
    int P[rows][cols];
    int Q[rows][cols];

    multiplyByFive(rows, cols, A, P);
    multiplyByFive(rows, cols, B, Q);

    // Print matrix P and Q
    printf("Massiv P:\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            printf("%d ", P[i][j]);
        }
        printf("\n");
    }
    printf("Massiv Q:");
    printf("\n");
    for(int i=0; i<rows; i++) {
        for(int j=0; j<cols; j++) {
            printf("%d ", Q[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}