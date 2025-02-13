#include <stdio.h>

// insertion sort
void insertion_sort(int code_list[], int size){
    for(int i = 1; i < size; i++){
        for(int j = i; j > 0 && code_list[j] < code_list[j-1]; j--){
            int temp = code_list[j];
            code_list[j] = code_list[j-1];
            code_list[j-1] = temp;
        }
    }
}

int main(){
    int code_list[] = {12, 11, 13, 5, 6, 14, 20};
    int size = sizeof(code_list) / sizeof(code_list[0]);

    insertion_sort(code_list, size);

    printf("Sorted array: ");
    for(int i = 0; i < size ; i++) {
        printf("%d ", code_list[i]);
    }
    
    return 0;
}
