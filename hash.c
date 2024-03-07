#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

// Hash table structure
struct HashTable {
  int keys[TABLE_SIZE];
  int values[TABLE_SIZE];
};

// Hash function
int hashFunction(int key) {
  return key % TABLE_SIZE;
}

// Insert key and value into hash table
void insert(struct HashTable* table, int key, int value) {
  int index = hashFunction(key);
  table->keys[index] = key;
  table->values[index] = value;
}

// Search for key in hash table and return index if found
int search(struct HashTable* table, int key) {
  int index = hashFunction(key);
  if(table->keys[index] == key) {
    return table->values[index];
  }
  return -1;
}

int main() {

  // Original array
  int arr[] = {12, 25, 32, 43, 54, 66, 5, 9, 17, 6};
  int n = sizeof(arr)/sizeof(arr[0]);
  
  // Create hash table
  struct HashTable table;
  
  // Insert keys and values 
  for(int i=0; i<n; i++) {
    insert(&table, arr[i], i); 
  }

  // Key to search
  int key = 66;
  
  // Search
  int index = search(&table, key);
  
  if(index == -1) {
    printf("Key not found\n");
  } else {
    printf("Key found at original index: %d\n", index);
  }

  return 0;
}
