def next_palindrome(number):
    number_str = str(number)
    length = len(number_str)
    
    # Handle all 9's case (like 999 -> 1001)
    if number_str == '9' * length:
        return int('1' + '0' * (length-1) + '1')
    
    # Get the left half including middle digit for odd length
    mid = (length + 1) // 2
    left = number_str[:mid]
    
    # Create palindrome by mirroring left half
    if length % 2 == 0:
        palindrome = left + left[::-1]
    else:
        palindrome = left + left[:-1][::-1]
    
    # If palindrome is greater than number, return it
    if int(palindrome) > number:
        return int(palindrome)
    
    # Otherwise increment the left half and mirror again
    left = str(int(left) + 1)
    
    # Handle carry over case
    if len(left) > mid:
        return int('1' + '0' * (length-1) + '1')
        
    if length % 2 == 0:
        palindrome = left + left[::-1]
    else:
        palindrome = left + left[:-1][::-1]
        
    return int(palindrome)

# Test the function
print(next_palindrome(18))










































