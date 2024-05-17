from math import log, sin


x_start = float(input('Введите начальное значение x: '))
x_finish = float(input('Введите конечное значение x: '))
x_step = float(input('Введите шаг значения x: '))

n = int((x_finish - x_start) / x_step) + 1
x = x_start

print('for loop:')
for i in range(n):
    if x < 0:
        y = log(x ** 2 + 1) + 2 * x
    elif x >= 0 and x < 2:
        y = sin(2 * x) ** 2
    else:
        y = pow(x ** 2 + x + 1, 0.5)

    print('x: {} y: {}'.format(x, y))
    x += x_step

x = x_start
print('while loop:')
while x <= x_finish:
    if x < 0:
        y = log(x ** 2 + 1) + 2 * x
    elif x >= 0 and x < 2:
        y = sin(2 * x) ** 2
    else:
        y = pow(x ** 2 + x + 1, 0.5)

    print('x: {} y: {}'.format(x, y))
    x += x_step

'''
#include <stdio.h>
#include <math.h>

int main() {
    float x_start, x_finish, x_step, x, y;
    int n, i;
    
    printf("Введите начальное значение x: ");
    scanf("%f", &x_start);
    printf("Введите конечное значение x: ");
    scanf("%f", &x_finish);
    printf("Введите шаг значения x: ");
    scanf("%f", &x_step);

    n = (int)((x_finish - x_start) / x_step) + 1;
    x = x_start;

    printf("for loop:\n");
    for (i = 0; i < n; i++) {
        if (x < 0) {
            y = log(pow(x, 2) + 1) + 2 * x;
        } else if (x >= 0 && x < 2) {
            y = pow(sin(2 * x), 2);
        } else {
            y = pow(x * x + x + 1, 0.5);
        }
        printf("x: %f y: %f\n", x, y);
        x += x_step;
    }

    x = x_start;
    printf("while loop:\n");
    while (x <= x_finish) {
        if (x < 0) {
            y = log(pow(x, 2) + 1) + 2 * x;
        } else if (x >= 0 && x < 2) {
            y = pow(sin(2 * x), 2);
        } else {
            y = pow(x * x + x + 1, 0.5);
        }
        printf("x: %f y: %f\n", x, y);
        x += x_step;
    }

    return 0;
}
'''