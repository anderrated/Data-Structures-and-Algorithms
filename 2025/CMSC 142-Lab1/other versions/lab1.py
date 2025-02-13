case_number = input("Enter number of test cases: ")
inputs = list(map(int, input("Enter multiple values: ").split()))

def palindrome_checker(number):
    original_number = number
    reversed = reverse(number)
    if (original_number == reversed):
        return True
    else:
        return False

def reverse(number):
    reversed = 0
    while number !=0:
        digit = number % 10
        reversed = reversed * 10 + digit
        number //= 10
    return reversed

def next_palindrome(number):
    for i in range(number+1, 1000):
        if palindrome_checker(i):
            print(i)
            break

print(list(map(next_palindrome, inputs)))
    