#include <stdio.h>

void quicksort(int arr[], int start, int end);
int partition(int arr[], int start, int end);

int main(){
    int arr[] = {13, 22, 57, 64, 99, 48, 57, 70};
    quicksort(arr, 0, 7);
    for (int i = 0; i < 8; i++) {
        printf("%d ", arr[i]);
    }
}

void quicksort(int arr[], int start, int end) {
    if (start < end) {
        int pIndex = partition(arr, start, end);
        quicksort(arr, start, pIndex - 1);
        quicksort(arr, pIndex + 1, end);
    }
}

int partition(int arr[], int start, int end) {
    int pivot = arr[end];
    int pIndex = start;
    for (int i = start; i < end; i++) {
        if (arr[i] <= pivot) {
            int temp = arr[i];
            arr[i] = arr[pIndex];
            arr[pIndex] = temp;
            pIndex++;
        }
    }
    int temp = arr[pIndex];
    arr[pIndex]= arr[end];
    arr[end] = temp;
    return pIndex;
}
