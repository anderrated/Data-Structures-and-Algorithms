"""
CMSC 142 Laboratory Exercise 1 Checker (by squiffy)
Instructions:
- Make sure that the "data" folder inside the "CMSC 142-Lab1.zip" file
    is in the same directory as this file
- Create a new folder in this directory and name it "output"
- Configure your Lab 1 code such that it will store the output of your
    program in the "output" folder and name them as "small_output" and
    "full_output" respectively
- Make sure that the format of the output files are exactly the same
    as with the format of the solution files
"""

print("Run checker for: (1) Small Input / (2) Full Input ?")
choice = input("Choice: ")
while (choice != "1" and choice != "2"):
    print("Invalid input!")
    choice = input("Choice: ")

import time

startTime = time.time()
choice = "small" if choice == "1" else "full"
solutionFile = open(f".\\data\\{choice}_solution", "r")
outputFile = open(f".\\output\\{choice}_output", "r")
itemCount = 0
mistakeCount = 0
solutionLine = solutionFile.readline()
outputLine = outputFile.readline()

print("\nChecking output for mistakes...")
while solutionLine:
    if (int(outputLine) != int(solutionLine)):
        print(f"Line {(itemCount + 1)}: Output = {int(outputLine)} | Solution = {int(solutionLine)}")
        mistakeCount = mistakeCount + 1
    solutionLine = solutionFile.readline()
    outputLine = outputFile.readline()
    itemCount = itemCount + 1
print(f"\nNumber of mistakes: {mistakeCount}")
print(f"Final result: {(itemCount - mistakeCount)}/{itemCount} = {(((itemCount - mistakeCount) / itemCount) * 100):.2f}% accuracy")

solutionFile.close()
outputFile.close()
endTime = time.time()
print(f"Time elapsed: {(endTime - startTime)} seconds")