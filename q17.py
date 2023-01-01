import re

# Create the file and add 10 mobile numbers to it
with open("abc.txt", "w") as file:
    for i in range(1, 11):
        file.write("912345678" + str(i) + "\n")

# Read the numbers from the file and filter them
filtered_numbers = []
with open("abc.txt", "r") as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if re.match(r"^[9,8,7,6]\d{9}$", line):  # Filter the numbers
            filtered_numbers.append(line)

# Write the filtered numbers to another file
with open("filtered_numbers.txt", "w") as file:
    for number in filtered_numbers:
        file.write(number + "\n")

# Print both files
print("Original file:")
with open("abc.txt", "r") as file:
    print(file.read())

print("\nFiltered numbers file:")
with open("filtered_numbers.txt", "r") as file:
    print(file.read())