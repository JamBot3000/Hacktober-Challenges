num = int(input("Enter a number: "))
while(num != 1):
    if((num % 2) == 0):  # even number = divide by 2
        num /= 2
    else:  # odd number = multiply by 3 and add 1
        num  = num * 3 + 1
    print(int(num))
print('Done!')
    