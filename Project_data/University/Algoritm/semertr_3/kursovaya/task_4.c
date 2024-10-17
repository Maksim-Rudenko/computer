#include <stdio.h>
#include <math.h>

// Определяем функции
double f1(double x) {
    return x / (x * x + 6 * x + 1);
}

double f2(double x) {
    return pow(10, 0.01 * x) * cos(0.125 * x);
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
    int num_func;
    
    printf("Введите нижнее основание интеграла: ");
    scanf("%lf", &lower_base);
    printf("Введите верхнее основание интеграла: ");
    scanf("%lf", &upper_base);
    
    int n = 1000; // Количество разбиений для интегрирования
    
    printf("Выберите функцию, для которой будет расчитан интеграл (1-3): ");
    scanf("%d", &num_func);

    if (num_func == 1) {
        printf("Интеграл f1 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f1, lower_base, upper_base, n));
    } else if (num_func == 2) {
        printf("Интеграл f2 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f2, lower_base, upper_base, n));
    } else {
        printf("Интеграл f3 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f3, lower_base, upper_base, n));
    }


    //printf("Интеграл f1 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f1, lower_base, upper_base, n));
    //printf("Интеграл f2 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f2, lower_base, upper_base, n));
    //printf("Интеграл f3 от %.2f до %.2f: %.6f\n", lower_base, upper_base, compute_integral(f3, lower_base, upper_base, n));
    
    return 0;
}