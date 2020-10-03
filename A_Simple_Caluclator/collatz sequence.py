'''Write a function named collatz() that has one parameter named number . If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1 .
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1 .'''

def collatz(n):
    value=n%2
    if value == 0:
        even=n//2
        return even   
    elif value == 1:
        odd=3*n+1
        return odd   
    else:
        return None

user_input=int(input('Enter a number:  '))
result=collatz(user_input)
print(result)
while result != 1:
    result=collatz(result)
    print(result)

