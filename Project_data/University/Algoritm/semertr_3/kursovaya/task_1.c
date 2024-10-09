#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define M_PI 3.14159265358979323846

// Функция для проверки, является ли строка целым числом
int is_integer(const char *str) {
    if (*str == '-' || *str == '+') str++; // Пропускаем знак числа
    if (!*str) return 0; // Пустая строка после знака
    while (*str) {
        if (!isdigit(*str)) return 0; // Если не цифра, возвращаем 0
        str++;
    }
    return 1;
}

// Функция для проверки, является ли строка числом с плавающей точкой
int is_float(const char *str) {
    int has_dot = 0;
    if (*str == '-' || *str == '+') str++; // Пропускаем знак числа
    if (!*str) return 0; // Пустая строка после знака
    while (*str) {
        if (*str == '.') {
            if (has_dot) return 0; // Если точка уже была, возвращаем 0
            has_dot = 1;
        } else if (!isdigit(*str)) {
            return 0; // Если не цифра и не точка, возвращаем 0
        }
        str++;
    }
    return 1;
}

// Функция расчета площади поверхности и объема шара
void function(int R, double result[2]) {
    result[0] = 4 * M_PI * R * R;
    result[1] = (4.0 / 3.0) * M_PI * R * R * R;
}


int main() {
    int r;
    double result[2];
    char input[100];
    int valid = 0;    

    while (!valid) {
        printf("Введите число: ");
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = 0; // Удаляем символ новой строки

        if (is_integer(input)){
            printf("Вы ввели целое число: %d\n", atoi(input));
            valid = 1;
            r = atoi(input);
            function(r, result);
            printf("%f %f\n", result[0], result[1]);            
        } else if (is_float(input)) {
            printf("Вы ввели число с плавающей точкой: %f\n", atof(input));
            valid = 1;
            r = atof(input);
            function(r, result);
            printf("%f %f\n", result[0], result[1]);  
        } 
          else {
            printf("Ошибка: введите корректное число.\n");
        }
    }

    return 0;
}