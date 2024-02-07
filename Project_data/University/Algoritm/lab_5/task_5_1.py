from math import atan

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
x_start = float(input('Введите начальное значение x: '))
x_finish = float(input('Введите начальное значение x: '))
x_step = int(input('Введите шаг значения x: '))


if x_start <= x_finish:
    while x_start <= x_finish:
        y = atan(a + x_start) / pow(a ** 3 + b ** 3, 0.5)    
        print('x: {} y: {}'.format(x_start, y))   
        x_start += x_step
else:
    while x_start >= x_finish:
        y = atan(a + x_start) / pow(a ** 3 + b ** 3, 0.5)    
        print('x: {} y: {}'.format(x_start, y))   
        x_start -= x_step



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
    
    another:
        printf("Введите шаг значения x: ");
        scanf("%d", &x_step);

    if (x_start > x_finish && x_step > 0) {
        printf("Если начальное значение х больше конечного, то шаг должен быть отрицательным\n");
        goto another;
    }
    
    while (x_start <= x_finish) {
        double y = atan(a + x_start) / sqrt(pow(a, 3) + pow(b, 3));
        printf("x: %lf y: %lf\n", x_start, y);
        x_start += x_step;
    }
    
    return 0;
}
'''
