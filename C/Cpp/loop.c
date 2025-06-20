#include <stdio.h>

int main(void) {
    
    
    for (int i = 1; i <= 10; i++) {
         printf("Hello World %d\n", i); // for (정수; 조건; 증감) {실행할 식}
    }
    
    printf("===============\n");

    int i = 1;
    while (i <= 10) {
        printf("Hello World %d\n", i++);
        //i++;
    }

    printf("===============\n");

    int j = 1;
    do{
        printf("Hello World %d\n", j++);
    } while (j <= 10);  // do{} while()은 먼저 실행하고 조건을 검사한다는 점에서 그냥 while () {} 과는 다름.

    printf("===============\n");


    for (int i = 1; i <= 3; i++) {
        printf("1st for loop: %d\n", i);\
        for (int j = 1; j <= 5; j++) {
            printf("    2nd for loop: %d\n", j);
        }
    }

    for (int a =0; a < 5; a++) {
        for (int b = 0; b <= a; b++) {
            printf("*");
        } printf("\n");
    }

    printf("역순 출력\n");

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5-(i+1); j++) {
            printf(" ");
        } for (int k = 0; k <= i; k++) {
            printf("*");
        } printf("\n");
    }

    return 0;
}