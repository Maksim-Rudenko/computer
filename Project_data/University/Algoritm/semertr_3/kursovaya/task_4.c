#include <stdio.h>
#include <math.h>
#include <string.h>

// Определяем заданные функции
double f1(double x) {
    return x / (x * x + 6 * x + 1);
}

double f2(double x) {
    return pow(10, -0.01 * x) * cos(0.125 * x);
}

double f3(double x) {
    return acos((3 * x + 25) / 100);
}

// Функция для вычисления интеграла методом Симпсона
double compute_integral(double (*func)(double), double a, double b, int n) {
    double h = (b - a) / n;
    double sum = func(a) + func(b);
    
    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        sum += (i % 2 == 0) ? 2 * func(x) : 4 * func(x);
    }
    
    return (h / 3) * sum;
}

int main() {
    double lower_base, upper_base;
    char num_func[100];
    
    // Ввод пределов интегрирования
    printf("Введите нижнее основание интеграла: ");
    scanf("%lf", &lower_base);
    printf("Введите верхнее основание интеграла: ");
    scanf("%lf", &upper_base);
    
    int n = 1000; // Количество разбиений для интегрирования
    
    // Выбор функции интегрирования
    printf("Выберите функцию, для которой будет расчитан интеграл (f1, f2, f3): ");
    scanf("%s", num_func);

    if (strcmp(num_func, "f1") == 0) {
        printf("Интеграл f1 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f1, lower_base, upper_base, n));
    } else if (strcmp(num_func, "f2") == 0) {
        printf("Интеграл f2 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f2, lower_base, upper_base, n));
    } else {
        printf("Интеграл f3 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f3, lower_base, upper_base, n));
    }   
    
    return 0;
}