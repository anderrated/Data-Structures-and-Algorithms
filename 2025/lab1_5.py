def next_palindrome(number):
    while True:
        number_str = str(number)
        left = 0
        right = len(number_str) - 1
        is_palindrome = True
        
        # Check pairs of digits moving inward
        while left < right:
            if number_str[left] != number_str[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
            
        if is_palindrome:
            return number
            
        number += 1

# Test the function
print(next_palindrome(1832))  # Output: 1881
