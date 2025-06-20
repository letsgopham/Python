#include <stdio.h>
#include <string.h>

int main(void) {
    /*char name[20];
    printf("이름을 입력하세요: ");
    scanf("%s", &name);

    char str[20];
    while (getchar() != '\n');
    printf("아무 문장을 입력하세요:\n");
    fgets(str, sizeof(str), stdin);

    str[strcspn(str, "\n")] = 0;

    if (strcmp(str, "Hello World!") == 0) {
        printf("Hello %s!", name);
    }
    else {
        printf("Welcome!");
    }*/

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