#include <stdio.h>

int main(void) {
    int a, b;

    if (scanf("%d%d", &a, &b) != 2) {
        puts("输入错误");
        return 1;
    }

    double avg = ((double)a + (double)b) / 2.0;
    printf("%.2f\n", avg);
    return 0;
}
