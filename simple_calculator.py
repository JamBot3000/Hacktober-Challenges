from math import *


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def div(x, y):
    return x / y


def mul(x, y):
    return x * y


def sq_root(x):
    return sqrt(x)


print("choose and operation from the list below:")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")
print("5.Square Root")

while True:
    operation = input("Select your operation (1/2/3/4/5): ")

    if operation in ('1', '2', '3', '4'):
        num1 = float(input("Enter your first value: "))
        num2 = float(input("Enter your second value: "))

        if operation == '1':
            print("Addition of ", num1, "and ", num2, "= ", add(num1, num2))

        elif operation == '2':
            print("Subtraction of ", num1, "and ", num2, "= ", sub(num1, num2))

        elif operation == '3':
            print("Division of ", num1, "and ", num2, "= ", div(num1, num2))

        elif operation == '4':
            print("multiplication of ", num1, "and ", num2, "= ", mul(num1, num2))
        break

    elif operation in '5':
        num = float(input("Enter your value: "))

        if operation == '5':
            print("Square root of ", num, "= ", sq_root(num))
        break

    else:
        print("Invalid Input")
