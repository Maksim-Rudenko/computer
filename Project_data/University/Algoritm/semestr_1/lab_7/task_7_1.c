#include <stdio.h>
#include <math.h>


int main() {
    
    int mas_len;

    array_len:
        printf("Enter length of array: ");
        scanf("%d", &mas_len);

    if (mas_len <= 0){
        printf("Length of array must be greater than zero\n");
        goto array_len;
    }

    float mas[mas_len];
    for (int i = 0; i < mas_len; i++) {
        printf("Enter array element: ");
        scanf("%f", &mas[i]);
    }

    float x, y;
    printf("Enter value X: ");
    scanf("%f", &x);

    another:
        printf("Enter value Y: ");
        scanf("%f", &y);

    if (y < x){
        printf("Value y must be greater than or equal to x\n");
        goto another;
    }

    float result_sum = 0;
    int result_count = 0;
    for (int i = 0; i < mas_len; i++) {
        if (mas[i] < x || mas[i] >= y) {
            result_sum += pow(mas[i], 2);
        }
        if (i % 2 != 0 && mas[i] < 0) {
            result_count += 1;
        }
    }

    printf("Start array: [");
    for (int i = 0; i < mas_len; i++) {
        printf("%.2f", mas[i]);
        if (i != mas_len - 1) {
            printf(", ");
        }
    }
    printf("]\n");
    printf("Interval [X, Y): [%.2f, %.2f)\n", x, y);
    printf("The sum of the squares of the numbers belonging to the interval [X, Y): %.2f\n", result_sum);
    printf("The number of negative numbers standing in even places: %d\n", result_count);

    return 0;
}