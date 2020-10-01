#This simple calculator, calculates with the four basic operators, Addition "+",
# Subtraction "-", Multiplication "*" and Division "/"

num1 = float(input ("enter your first number: "))
#float actually converted whatever the user inputed from a string to a number, either integer or decimal
op = input ("enter your operator ")
num2 = float(input ("enter your second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
