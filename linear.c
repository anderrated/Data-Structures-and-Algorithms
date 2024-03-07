#include <stdio.h>

int linear() {
    int arr[] = {12, 11, 13, 5, 6, 14, 20};
    int size = sizeof(arr) / sizeof(arr[0]);
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    for (int i = 0; i < size; i++) {
        if (num == arr[i]) {
            printf("Number found at index %d", i);
        }
    }

    return 0;
}