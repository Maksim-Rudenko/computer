'''
Отсортировать массив по неубыванию методом включения с 
выбором включаемого элемента слева направо

#include <stdio.h>

#define maxcount 100

typedef struct {
    int arr[maxcount + 1];
} tarray;

tarray inputarray() {
    tarray a;
    int i;
    printf("размер массива: ");
    scanf("%d", &a.arr[0]);
    printf("элементы: ");
    for (i = 1; i <= a.arr[0]; i++) {
        scanf("%d", &a.arr[i]);
    }
    return a;
}

void order(tarray *a) {
    int i, j, t;
    for (i = 2; i <= a->arr[0]; i++) {
        t = a->arr[i];
        j = i - 1;
        while (j > 0 && a->arr[j] > t) {
            a->arr[j + 1] = a->arr[j];
            a->arr[j] = t;
            j--;
        }
    }
}

void outarray(tarray a) {
    int i;
    for (i = 1; i <= a.arr[0]; i++) {
        printf(" %d", a.arr[i]);
    }
    printf("\n");
}

int main() {
    tarray ar;
    printf("Вводимый массив:\n");
    ar = inputarray();
    order(&ar);
    
    printf("результат\n");
    printf("первый\n");
    outarray(ar);
    
    return 0;
}
'''