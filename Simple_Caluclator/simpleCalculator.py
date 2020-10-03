# Python program of a simple calculator

# This function performs addition of two number's
def add(num_one, num_two):
    return num_one + num_two

# This function performs subtraction of two number's
def subtract(num_one, num_two):
    return num_one - num_two

# This function performs multiplication of two number's
def multiply(num_one, num_two):
    return num_one * num_two

# This function performs division of two number's
def divide(num_one, num_two):
    return num_one / num_two

# Selection of operation
print("Please select the operation you would like to perform.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    # Take choice from the user
    choice = input("Enter your choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        
        # Take input of first and second number from the user 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Check which operation to perform 
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    
    else:
        print("Invalid Input")