'''В упорядоченном по возрастанию массиве чисел определить,
есть ли заданное число А, и найти произведение квадратов чисел, меньших А.'''

mas_len = int(input('Введите длину массива: '))
mas = []
for i in range(mas_len):
    val = float(input('Введите элемент массива: '))
    mas.append(val)

A = float(input('Введите число А: '))

print("Исходный массив:\n{}".format(mas))

# Алгоритм быстрой сортировки массива
def partition(sort_nums, begin, end):
    part = begin
    for i in range(begin + 1, end + 1):
        if sort_nums[i] <= sort_nums[begin]:
            part += 1
            sort_nums[i], sort_nums[part] = sort_nums[part], sort_nums[i]
    sort_nums[part], sort_nums[begin] = sort_nums[begin], sort_nums[part]
    return part

def quick_sort(sort_nums, begin=0, end=None):
    if end is None:
        end = len(sort_nums) - 1
    def quick(sort_nums, begin, end):
        if begin >= end:
            return
        part = partition(sort_nums, begin, end)
        quick(sort_nums, begin, part - 1)
        quick(sort_nums, part + 1, end)
    return quick(sort_nums, begin, end)

# Сортировка массива по возрастанию
quick_sort(mas)

result = 1
quest = 0


# Расчет произведения квадратов чисел, меньших А; определение есть ли число А в массиве
for i in range(len(mas)):
    if mas[i] < A:
        result *= mas[i] ** 2
    elif mas[i] == A:
        quest = 1
    

print("Отсортированный массив:\n{}".format(mas))
print("Есть ли заданное число А ({}) в исходном массиве: {}".format(A, quest == 1))
print("Произведение квадратов чисел, меньших А ({}): {}".format(A, result))


'''
#include <stdio.h>

int partition(float sort_nums[], int begin, int end) {
    int part = begin;
    for (int i = begin + 1; i <= end; i++) {
        if (sort_nums[i] <= sort_nums[begin]) {
            part += 1;
            float temp = sort_nums[i];
            sort_nums[i] = sort_nums[part];
            sort_nums[part] = temp;
        }
    }
    float temp = sort_nums[part];
    sort_nums[part] = sort_nums[begin];
    sort_nums[begin] = temp;
    return part;
}

void quick_sort(float sort_nums[], int begin, int end) {
    if (begin >= end) {
        return;
    }
    int part = partition(sort_nums, begin, end);
    quick_sort(sort_nums, begin, part - 1);
    quick_sort(sort_nums, part + 1, end);
}

int main() {
    int mas_len;
    printf("Введите длину массива: ");
    scanf("%d", &mas_len);
    float mas[mas_len];
    for (int i = 0; i < mas_len; i++) {
        printf("Введите элемент массива: ");
        scanf("%f", &mas[i]);
    }
    float A;
    printf("Введите число А: ");
    scanf("%f", &A);

    printf("Исходдный массив:\n");
    for (int i = 0; i < mas_len; i++) {
        printf("%f ", mas[i]);
    }

    quick_sort(mas, 0, mas_len - 1);

    int result = 1;
    int quest = 0;   

    for (i = 0; i < sizeof(mas) / sizeof(mas[0]); i++) {
        if (mas[i] < A) {
            result *= mas[i] * mas[i];
        } else if (mas[i] == A) {
            quest = 1;
        }
    }

    printf("Отсортированный массив:\n");
    for (int i = 0; i < mas_len; i++) {
        printf("%f ", mas[i]);
    }
    printf("\n");
    printf("Есть ли заданное число А (%f) в исходном массиве: %s\n", A, quest == 1 ? "Да" : "Нет");
    printf("Произведение квадратов чисел, меньших А (%f): %d\n", A, result);

    return 0;
}
'''