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

// binary search
int binary_search(int code_list[], int size, int target) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (code_list[mid] == target)
            return mid;
        else if (code_list[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1; // Not found
}

int main(){
    int code_list[] = {12, 11, 13, 5, 6, 14, 20};
    int size = sizeof(code_list) / sizeof(code_list[0]);
    int target;
    
    insertion_sort(code_list, size);

    printf("Sorted array: ");
    for(int i = 0; i < size ; i++) {
        printf("%d ", code_list[i]);
    }
    
    // Binary search example
    printf ("\nEnter target value: ");
    scanf ("%d", &target);
    int result = binary_search(code_list, size, target);
    if (result != -1)
        printf("\n%d found at index %d\n", target, result);
    else
        printf("\n%d not found\n", target);

    return 0;
}
