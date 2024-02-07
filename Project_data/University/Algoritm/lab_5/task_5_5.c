#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
    int k;
    printf("Enter a number k: ");
    scanf("%d", &k);

    char sequence[1000];
    int degree = 0;

    while (strlen(sequence) < k) {
        int num = pow(5, degree);
        char temp[10];
        sprintf(temp, "%d", num);
        strcat(sequence, temp);
        degree++;
    }

    printf("%s\n", sequence);
    printf("%c\n", sequence[k - 1]);

    return 0;
}