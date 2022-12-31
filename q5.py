print("Choose operation for calculator:")
print("1. Add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. MODULUS")
print("6. FLOOR VALUE")
print("7. EXPONENT")

operation = input("Enter your choice:\n")

if operation == "1":
    num1 = input("Enter first number for Addition:\n")
    num2 = input("Enter second number for Addition:\n")
    print("The Addition of these numbers is:",int(num1)+int(num2))
elif operation == "2":
    num1 = input("Enter first number for Subtraction:\n")
    num2 = input("Enter second number for Subtraction:\n")
    print("The Subtraction of these numbers is:",int(num1)-int(num2))
elif operation == "3":
    num1 = input("Enter first number for Multiplication:\n")
    num2 = input("Enter second number for Multiplication:\n")
    print("The Multiplication of these numbers is:",int(num1)*int(num2))
elif operation == "4":
    num1 = input("Enter first number for Division:\n")
    num2 = input("Enter second number for Division:\n")
    print("The Division of these numbers is:",int(num1)/int(num2))
elif operation == "5":
    num1 = input("Enter first number for Modulus operation:\n")
    num2 = input("Enter second number for Modulus operation:\n")
    print("The Modulus value of these numbers is:",int(num1)%int(num2))
elif operation == "6":
    num1 = input("Enter first number for Floor operation:\n")
    num2 = input("Enter second number for Floor operation:\n")
    print("The Floor value of these numbers is:",int(num1)//int(num2))
elif operation == "7":
    num1 = input("Enter first number for Exponent:\n")
    num2 = input("Enter second number for Exponent:\n")
    print("The Exponent value of these numbers is:",(int(num1)**int(num2)))
else:
    print("You entered an Invalid option!")

