def next_palindrome(number):
    number_str = str(number)
    digit_count = len(number_str)
    
    # Split into left and right
    left_half = number_str[:digit_count // 2]  
    right_half = number_str[digit_count // 2:]  
    leftmost_digit = int(left_half[0])
    rightmost_digit = int(right_half[-1])
 

    while rightmost_digit != leftmost_digit:
        number += 1 # increment number until the rightmost digit is equal to the leftmost digit
        # Update the rightmost digit to the new rightmost digit
        rightmost_digit = int(str(number)[-1])
        # Update the leftmost digit to the new leftmost digit
        leftmost_digit = int(str(number)[0])
    return number
    
print(next_palindrome(1832)) 

