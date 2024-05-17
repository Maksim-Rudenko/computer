#include <stdio.h>

int main() {
    int N, M;
    
    // Ввод размерности матрицы
    printf("Enter the number of rows of the matrix: ");
    scanf("%d", &N);
    printf("Enter the number of columns of the matrix: ");
    scanf("%d", &M);
    
    // Ввод элементов матрицы
    int matrix[N][M];
    for (int i = 0; i < N; i++) {
        printf("Enter the elements of the row number %d of the matrix separated by a space: ", i+1);
        for (int j = 0; j < M; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // Вычисление количества положительных элементов в строках с нечетными номерами
    int count = 0;
    for (int i = 0; i < N; i++) {
        if ((i + 1) % 2 != 0) {  // Нечетный номер строки
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] > 0) {  // Положительный элемент
                    count++;
                }
            }
        }
    }
    
    // Вывод исходной матрицы и результата вычислений
    printf("The original matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("The number of positive elements in rows with odd numbers: %d\n", count);
    
    return 0;
}