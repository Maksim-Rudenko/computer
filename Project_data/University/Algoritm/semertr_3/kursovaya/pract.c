#include <stdio.h>
#include <math.h>

void function(int R, double result[2]) {
    result[0] = 4 * M_PI * R * R;
    result[1] = (4.0 / 3.0) * M_PI * R * R * R;
}

int main() {
    int r;
    double result[2];

    scanf("%d", &r);
    function(r, result);
    printf("[%f, %f]\n", result[0], result[1]);

    return 0;
}