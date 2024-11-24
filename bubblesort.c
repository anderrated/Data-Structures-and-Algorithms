#include <stdio.h>

int main() {
    int array[] = {9, 1, 8, 2, 7, 3, 6, 4, 5};

    int size = sizeof(array) / sizeof(array[0]);

    for (int i = 0; i < size; i++){
        printf("%d ", array[i]);
    }

    return 0;
}

