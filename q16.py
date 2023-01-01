# Get the employee name and address from the user
name = input("Enter employee name: ")
address = input("Enter employee address: ")

# Create the file and write the employee name and address to it
with open("abc.txt", "w") as file:
    file.write(name + "\n")
    file.write(address + "\n")

print("Employee information written to file successfully.")
