#include <stdio.h>

void min_heapify(int arr[], int i, int heap_size);
void build_min_heap(int arr[], int heap_size);

int main(){
    int arr[] = {13, 22, 57, 64, 99, 48, 57, 70};
    int heap_size = sizeof(arr)/sizeof(arr[0]);
    build_min_heap(arr, heap_size);
    for (int i = 0; i < heap_size; i++){
        printf("%d ", arr[i]);
    }
}

void min_heapify(int arr[], int i, int heap_size){ //array, root, heap size
    int smallest;
    int left = 2*i+1;
    int right = 2*i+2;

    if (left < heap_size && arr[left] < arr[i]){
        smallest = left;
    }
    else{
        smallest = i;
    }
    if (right < heap_size && arr[right] < arr[smallest]){
        smallest = right;
    }
    if (smallest != i){
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
        min_heapify(arr, smallest, heap_size);
    }
}

void build_min_heap(int arr[], int heap_size){
    for (int i = heap_size/2; i >= 0; i--){
        min_heapify(arr, i, heap_size);
    }
}

