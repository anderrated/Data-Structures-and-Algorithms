#include <stdio.h>

void quicksort(int arr[], int start, int end);
int partition(int arr[], int start, int end);

int main(){
    int arr[] = {13, 22, 57, 64, 99, 48, 57, 70};
    quicksort(arr, 0, 7);
    for (int i = 0; i <= 7; i++) {
        printf("%d ", arr[i]);
    }
}

void quicksort(int arr[], int start, int end) {
    if (start < end) {
        int pIndex = partition(arr, start, end);
        quicksort(arr, start, pIndex - 1); // recurse left
        quicksort(arr, pIndex + 1, end); // recurse right
    }
}

int partition(int arr[], int start, int end) {
    int pivot = arr[end]; // element
    int pIndex = start; // index
    for (int i = start; i < end; i++) {
        // if element is greater than pivot, ignore
        if (arr[i] <= pivot) {
            // swap element with pIndex
            int temp = arr[i];
            arr[i] = arr[pIndex];
            arr[pIndex] = temp;
            pIndex++;
        }
    }
    // swap pivot with pIndex
    int temp = arr[pIndex];
    arr[pIndex]= arr[end];
    arr[end] = temp;
    return pIndex;
}
