#include <stdio.h>

int main(void) {
    int a, b;

    if (scanf("%d%d", &a, &b) != 2) {
        puts("输入错误");
        return 1;
    }

    int max_value = (a > b) ? a : b;
    printf("%d\n", max_value);
    return 0;
}
