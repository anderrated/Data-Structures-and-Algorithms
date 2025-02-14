import os

# get directory of this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# output and data folder in script directory
output_dir = os.path.join(script_dir, "output")
data_dir = os.path.join(script_dir, "data")

os.makedirs(output_dir, exist_ok=True)

# file paths
full_input_path = os.path.join(data_dir, "full_input")
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
            # Carry
            x = j - 1
            while digits[x] >= 10:
                digits[x] %= 10
                x -= 1
                digits[x] += 1

        digits[j] = digits[i]
        i += 1
        j -= 1

    return make_int(digits)

# input for small test cases
test_count = int(input("Enter number of test cases: "))
print("Enter test cases: ")

small_test_list = [int(input()) for _ in range(test_count)]

# read full input from file and skip the first line
with open(full_input_path, "r") as file:
    full_test_list = [int(line.strip()) for i, line in enumerate(file) if i > 0]  # skip first line

# results
small_results = [next_palindrome(n) for n in small_test_list]
full_results = [next_palindrome(n) for n in full_test_list]

# write results to small_output
with open(small_output_path, "w") as small_file:
    for palindrome in small_results:
        small_file.write(f"{palindrome}\n")

# write results to full_output
with open(full_output_path, "w") as full_file:
    for palindrome in full_results:
        full_file.write(f"{palindrome}\n")

print(f"\nOutputs saved to '{small_output_path}' and '{full_output_path}'.")