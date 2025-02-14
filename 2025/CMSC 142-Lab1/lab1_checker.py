import filecmp

small_solution = open("C:\Users\ASUS\Desktop\BSCS 3 -  2nd Sem\CMSC 142\Data-Structures-and-Algorithms\Data-Structures-and-Algorithms\2025\CMSC 142-Lab1\data\small_solution", "r")
full_solution = open("C:\Users\ASUS\Desktop\BSCS 3 -  2nd Sem\CMSC 142\Data-Structures-and-Algorithms\Data-Structures-and-Algorithms\2025\CMSC 142-Lab1\data\full_solution", "r")
small_output = open("C:\Users\ASUS\Desktop\BSCS 3 -  2nd Sem\CMSC 142\Data-Structures-and-Algorithms\Data-Structures-and-Algorithms\2025\CMSC 142-Lab1\output\small_output", "r")
full_output = open("C:\Users\ASUS\Desktop\BSCS 3 -  2nd Sem\CMSC 142\Data-Structures-and-Algorithms\Data-Structures-and-Algorithms\2025\CMSC 142-Lab1\output\full_output", "r")

small_solution_data = small_solution.readlines()
small_output_data
full_solution_data = full_solution.readlines()

print("Checking output for mistakes...")
choice = input("Enter checker type (1 = small input, any number = full input): ")

if (choice == 1):
    i = 0
    for line1 in small_solution
    result = filecmp.cmp(small_output, small_solution)
    print(result)
else:
    result = filecmp.cmp(full_output, full_solution)
    print(result)

