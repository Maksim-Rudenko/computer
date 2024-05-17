#include <stdio.h>
#include <math.h>

int main() {
    double a, b, x_start, x_finish;
    int x_step;
    
    printf("Enter num a: ");
    scanf("%lf", &a);
    
    printf("Enter num b: ");
    scanf("%lf", &b);
    
    printf("Enter start value x: ");
    scanf("%lf", &x_start);
    
    printf("Enter finish value x: ");
    scanf("%lf", &x_finish);
    
    printf("Enter step value x: ");
    scanf("%d", &x_step);

    
    if (x_start <= x_finish) {
    while (x_start <= x_finish) {
        double y = atan(a + x_start) / sqrt(pow(a, 3) + pow(b, 3));
        printf("x: %f y: %f\n", x_start, y);
        x_start += x_step;
        }
    } else {
    while (x_start >= x_finish) {
        double y = atan(a + x_start) / sqrt(pow(a, 3) + pow(b, 3));
        printf("x: %f y: %f\n", x_start, y);
        x_start -= x_step;
        }
    }
    
    return 0;
}