#include <stdio.h>

void mergesort(int arr[], int size);
void merge(int left[], int left_size, int right[], int right_size, int arr[]);

int main() {
    int arr[] = {51,42,3,43,52,16,57,8,19,10};
    int size = 10;
    mergesort(arr, size);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

void mergesort(int arr[], int size) {
    if (size < 2) {
        return;
    } 

    int mid = size/2;
    int left[mid];
    int right[size-mid];

    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }
    for (int i = mid; i < size; i++) {
        right[i-mid] = arr[i];
    }
    mergesort(left, mid);
    mergesort(right, size-mid);
    merge(left, mid, right, size-mid, arr);
}

void merge(int left[], int left_size, int right[], int right_size, int arr[]) {
    int i = 0;
    int j = 0;
    int k = 0;
    while (i < left_size && j < right_size) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while(i < left_size) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while(j < right_size) {
        arr[k] = right[j];
        j++;
        k++;
    }
}