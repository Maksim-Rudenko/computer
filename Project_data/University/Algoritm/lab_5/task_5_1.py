from math import atan

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
x_start = float(input('Введите начальное значение x: '))
x_finish = float(input('Введите начальное значение x: '))
x_step = int(input('Введите шаг значения x: '))

while x_start <= x_finish:
    y = atan(a + x_start) / pow(a ** 3 + b ** 3, 0.5)    
    print('x: {} y: {}'.format(x_start, y))
    
    x_start += x_step


'''
#include <stdio.h>
#include <math.h>

int main() {
    double a, b, x_start, x_finish;
    int x_step;
    
    printf("Введите значение a: ");
    scanf("%lf", &a);
    
    printf("Введите значение b: ");
    scanf("%lf", &b);
    
    printf("Введите начальное значение x: ");
    scanf("%lf", &x_start);
    
    printf("Введите конечное значение x: ");
    scanf("%lf", &x_finish);
    
    printf("Введите шаг значения x: ");
    scanf("%d", &x_step);
    
    while (x_start <= x_finish) {
        double y = atan(a + x_start) / sqrt(pow(a, 3) + pow(b, 3));
        printf("x: %lf y: %lf\n", x_start, y);
        x_start += x_step;
    }
    
    return 0;
}
'''
