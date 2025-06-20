#include <stdio.h>

int main(void) {
for (int d = 2; d <=9; d++) {
    printf("    %d단      ",d);
} printf("\n");

for (int i = 1; i <= 10; i++) {
    for (int j = 2; j <= 9; j++) {
        printf("%d x %d = %d    ", j, i, j*i);
    }
    printf("\n");
}
    return 0;
}