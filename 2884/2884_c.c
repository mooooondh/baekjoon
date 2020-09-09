#include <stdio.h>

int main()
{
    int h;
    int m;
    scanf("%d", &h);
    scanf("%d", &m);

    if (m >= 45) {
        m -= 45;
        printf("%d %d", h, m);
    }
    else {
        if (h == 0) {
            h = 24;
        }
        h -= 1;
        m += 15;
        printf("%d %d", h, m);
    }
}