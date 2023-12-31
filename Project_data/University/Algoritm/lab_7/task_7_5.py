'''Известна масса (кг) каждой из M деталей, изготавливаемых на предприятии. 
Известна также масса заготовки для каждой детали.
Найти максимальные массы заготовок и деталей. Определить количество 
деталей, у которых отходы больше 10% (отходы вычисляются как отношение 
разности между массой заготовки и массой детали к массе заготовки и 
выражаются в %).'''


# Число деталей М
M = int(input('Введите количество деталей: '))

# Массив масс детелей
M_mass = []
for i in range(M):
    val = float(input('Введите массу {}-й детали: '.format(i + 1)))
    M_mass.append(val)

# Массив масс заготовок
billet_mass = []
for i in range(M):
    val = float(input('Введите массу {}-й заготовки: '.format(i + 1)))
    billet_mass.append(val)

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

# Сортировка массивов по возрастанию
quick_sort(M_mass)
quick_sort(billet_mass)

result = 0

for i in range(M):
    if (billet_mass[i] - M_mass[i]) / billet_mass[i] > 0.1:
        result += 1


print(M_mass)
print(billet_mass)
print("Количество деталей, у которых отходы больше 10%: {}".format(result))


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
    int M;
    printf("Введите количество деталей: ");
    scanf("%d", &M);

    float M_mass[M];
    for (int i = 0; i < M; i++) {
        printf("Введите массу %d-й детали: ", i + 1);
        scanf("%f", &M_mass[i]);
    }

    float billet_mass[M];
    for (int i = 0; i < M; i++) {
        printf("Введите массу %d-й заготовки: ", i + 1);
        scanf("%f", &billet_mass[i]);
    }

    quick_sort(M_mass, 0, M - 1);
    quick_sort(billet_mass, 0, M - 1);

    int result = 0;
    for (int i = 0; i < M; i++) {
        if ((billet_mass[i] - M_mass[i]) / billet_mass[i] > 0.1) {
            result += 1;
        }
    }

    printf("Количество деталей, у которых отходы больше 10%%: %d\n", result);

    return 0;
}

'''