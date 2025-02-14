import os

# get directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# output folder in script directory
output_dir = os.path.join(script_dir, "output")
os.makedirs(output_dir, exist_ok=True)

# file paths
small_output_path = os.path.join(output_dir, "small_output")
full_output_path = os.path.join(output_dir, "full_output")

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

# print()
# for n in test_list:
#     print(next_palindrome(n))

# compute results
results = [(n, next_palindrome(n)) for n in test_list]

# write results to files
with open(small_output_path, "w") as small_file, open(full_output_path, "w") as full_file:
    for original, palindrome in results:
        small_file.write(f"{palindrome}\n")
        full_file.write(f"{original} -> {palindrome}\n")

print(f"\nOutputs saved to '{small_output_path}' and '{full_output_path}'.")