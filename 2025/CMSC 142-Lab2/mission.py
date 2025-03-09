number_of_cases = int(input("Enter the number of problems to be solved:"))

number_of_missions = int(input("Enter the number of missions:"))

array = []

for mission in range(number_of_missions):
    user_input = input("Enter the mission name, day of arrival, and mission length:").split()
    print("Mission name:", user_input[0])
    print("Day of arrival:", user_input[1])
    print("Mission length:", user_input[2])
    array.append(user_input)
    print(array)

