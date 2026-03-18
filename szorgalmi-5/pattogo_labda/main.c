#include <stdio.h>
#include <Windows.h>

#define WIDTH 120
#define HEIGHT 30

int main()
{
    int x = 0, y = 0;
    int dx = 1, dy = 1;

    printf("\033[?25l");

    while (1)
    {
        printf("\033[%d;%dH ", y + 1, x + 1);

        x += dx;
        y += dy;

        if (x <= 0 || x >= WIDTH - 1)  dx = -dx;
        if (y <= 0 || y >= HEIGHT - 1) dy = -dy;

        printf("\033[%d;%dHO", y + 1, x + 1);

        fflush(stdout);
        Sleep(16);
    }

    return 0;
}
