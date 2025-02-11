# extract list of digits out of an integer
def extract_digits(n: int) -> list[int]:
    return list(map(int, str(n)))

# concat list of digits back to an integer
def make_int(digits: list[int]) -> int:
    return int("".join(map(str, digits)))

def next_palindrome(n: int) -> int:
    n += 1
    digits = extract_digits(n)

    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[j] > digits[i]:
            digits[j - 1] += 1

        digits[j] = digits[i]
        i += 1
        j -= 1

    return make_int(digits)

test_count = int(input("Enter number of test cases: "))
print("Enter test cases: ")

test_list = []
for _ in range(test_count):
    test_list.append(int(input()))

print()
for n in test_list:
    print(next_palindrome(n))