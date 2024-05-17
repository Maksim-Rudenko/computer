'''
Отсортировать массив по невозрастанию методом обменов 
рядом стоящих элементов с фиксированным числом 
просмотров, направленных слева направо

Ставит вместо 1-го (самого большого элемента) последний (самый маленький)
хотя я не вижу ошибки...


#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] < arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {5, 2, 9, 1, 7};
    int n = sizeof(arr)/sizeof(arr[0]);
  
    bubbleSort(arr, n);
  
    printf("Отсортированный массив: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}





'''