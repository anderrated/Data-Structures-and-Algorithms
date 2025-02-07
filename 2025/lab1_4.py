def extract_digits(n: int) -> list[int]:
    return list(map(int, str(n)))

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

test_count = int(input())
inputs = []
for _ in range(test_count):
    inputs.append(int(input()))

for n in inputs:
    print(next_palindrome(n))

# for n in [0, 18, 934, 5, 757, 1234, 1421, 1420, 1992, 19900, 18999]:
#     print(n, next_palindrome(n))
