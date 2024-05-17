'''
В матрице размером M*N переставить столбцы таким образом, 
чтобы получилась последовательность С1≤С2≤… ≤ Сj ≤…≤ СM, где 
Сj– сумма абсолютных значений элементов j-ого столбца 
(j=1,2,…,M).
'''

arr = [[1,2,37,4,50], 
       [6,7,7,9,17], 
       [41,2,13,1,15]] 
# M = 5 число столбцов
# N = 3 число строк

M = len(arr[0])
N = len(arr)

sum_val = []

for i in range(M):
    col_abs_sum = 0
    for j in range(N):
        col_abs_sum += arr[j][i]

    sum_val.append(col_abs_sum)

arr.append(sum_val)
for i in arr:
    print(", ".join([str(l).rjust(3) for l in i]))

for i in range(M):
    for k in range(i+1, M):
        if arr[N][i] > arr[N][k]:
            for j in range(N + 1):
                temp = arr[j][i]
                arr[j][i] = arr[j][k]
                arr[j][k] = temp

del arr[N]

print('================================================================')
for i in arr:
    print(", ".join([str(l).rjust(3) for l in i]))


'''
#include <stdio.h>
#include <stdlib.h>

int main() {
    int arr[3][5] = {
        {1, 2, 37, 4, 50},
        {6, 7, 7, 9, 17},
        {41, 2, 13, 1, 15}
    };

    int M = sizeof(arr[0]) / sizeof(arr[0][0]);
    int N = sizeof(arr) / sizeof(arr[0]);
    int sum_val[5] = {0};
    int i, j, k, temp;

    for (i = 0; i < M; i++) {
        int col_abs_sum = 0;
        for (j = 0; j < N; j++) {
            col_abs_sum += arr[j][i];
        }
        sum_val[i] = col_abs_sum;
    }

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            printf("%3d", arr[i][j]);
            if (j < M - 1) {
                printf(", ");
            }
        }
        printf("\n");
    }

    for (i = 0; i < M; i++) {
        for (k = i + 1; k < M; k++) {
            if (sum_val[i] > sum_val[k]) {
                for (j = 0; j < N; j++) {
                    temp = arr[j][i];
                    arr[j][i] = arr[j][k];
                    arr[j][k] = temp;
                }
                temp = sum_val[i];
                sum_val[i] = sum_val[k];
                sum_val[k] = temp;
            }
        }
    }

    printf("================================================================\n");

    for (i = 0; i < N; i++) {
        for (j = 0; j < M; j++) {
            printf("%3d", arr[i][j]);
            if (j < M - 1) {
                printf(", ");
            }
        }
        printf("\n");
    }

    return 0;
}

'''

