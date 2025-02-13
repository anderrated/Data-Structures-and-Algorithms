#include <stdio.h>

void max_heapify(int arr[], int i, int heap_size);
void build_max_heap(int arr[], int heap_size);

int main(){
    int arr[] = {13, 22, 57, 64, 99, 48, 57, 70};
    int heap_size = sizeof(arr)/sizeof(arr[0]);
    build_max_heap(arr, heap_size);
    for (int i = 0; i < heap_size; i++){
        printf("%d ", arr[i]);
    }
}

void max_heapify(int arr[], int i, int heap_size){ //array, root, heap size
    int largest;
    int left = 2*i+1;
    int right = 2*i+2;

    if (left < heap_size && arr[left] > arr[i]){
        largest = left;
    }
    else{
        largest = i;
    }
    if (right < heap_size && arr[right] > arr[largest]){
        largest = right;
    }
    if (largest != i){
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        max_heapify(arr, largest, heap_size);
    }
}

void build_max_heap(int arr[], int heap_size){
    for (int i = heap_size/2; i >= 0; i--){
        max_heapify(arr, i, heap_size);
    }
}

