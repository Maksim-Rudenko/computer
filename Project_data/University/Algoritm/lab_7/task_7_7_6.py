
'''
Отсортировать массив по неубыванию методом распределения по 
массиву ключей, упорядоченному по неубыванию. 
'''
# здесь из интернета по невозрастанию!!!!

class Massiv:
    def partition(self, arr, start, end):
        marker = start
        for i in range(start, end):
            if arr[i] < arr[end]:
                arr[i], arr[marker] = arr[marker], arr[i]
                marker += 1
        arr[marker], arr[end] = arr[end], arr[marker]
        return marker

    def quicksort(self, arr, start, end):
        if start >= end:
            return
        pivot = self.partition(arr, start, end)
        self.quicksort(arr, start, pivot - 1)
        self.quicksort(arr, pivot + 1, end)


'''

#include <stdio.h>

int partition(int arr[], int start, int end) {
    int marker = start;
    int tmp;
    for (int i = start; i < end; i++) {
        if (arr[i] < arr[end]) {
            tmp = arr[marker];
            arr[marker] = arr[i];
            arr[i] = tmp;
            marker += 1;
        }
    }
    tmp = arr[marker];
    arr[marker] = arr[end];
    arr[end] = tmp;
    return marker;
}

void quicksort(int arr[], int start, int end) {
    if (start >= end) {
        return;
    }
    int pivot = partition(arr, start, end);
    quicksort(arr, start, pivot - 1);
    quicksort(arr, pivot + 1, end);
}

int main() {
    int arr[] = {5, 2, 9, 1, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    quicksort(arr, 0, n - 1);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
'''



#youchat
'''
#include <stdio.h>

void countingSort(int arr[], int n, int max) {
    int count[max+1];
    int output[n];
    
    for (int i = 0; i <= max; i++) {
        count[i] = 0;
    }
    
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }
    
    for (int i = 1; i <= max; i++) {
        count[i] += count[i-1];
    }
    
    for (int i = n-1; i >= 0; i--) {
        output[count[arr[i]]-1] = arr[i];
        count[arr[i]]--;
    }
    
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

int main() {
    int arr[] = {5, 2, 9, 1, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
  
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
  
    countingSort(arr, n, max);
  
    printf("Упорядоченный по неубыванию массив: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
'''