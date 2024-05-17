#  Дано натуральное k. Определить k-ю цифру последовательности: 
#1525125625..., в которой выписаны подряд степени 5.

k = int(input("Введите число k: "))

sequence = ''
degree = 0

while len(sequence) < k:
    sequence += str(pow(5, degree))
    degree += 1

print(sequence)
print(sequence[k - 1])

'''
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
'''