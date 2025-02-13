case_number = int(input("Enter number of test cases: "))
inputs = list(map(int, input("Enter multiple values: ").split()))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_smallest_palindrome(n):
    n += 1 
    while not is_palindrome(n):
        n += 1
    return n

for num in inputs:
    print(next_smallest_palindrome(num))
