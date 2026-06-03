#include <stdio.h>

int main(void) {
    int a, b;

    if (scanf("%d%d", &a, &b) != 2) {
        puts("输入错误");
        return 1;
    }

    if (b == 0) {
        puts("除数不能为0");
        return 1;
    }

    printf("%d\n", a % b);
    return 0;
}
