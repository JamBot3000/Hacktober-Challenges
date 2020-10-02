# A palindrome is nothing but any number or a string which remains unaltered when reversed.
def palindrome():
    # check if user input is palindrome or not
    Input = input("Enter a number or string\t")
    if Input.isdigit():
        Input = int(Input)
        rev = 0                     # Reverse of number
        temp = Input
        while Input > 0:            #Loop through number backwards
            rem = Input % 10
            rev = rev * 10 + rem
            Input = Input // 10
        if temp == rev:
            print(str(temp) + " is a Palindrome number")
        else:
            print(str(temp) + " is NOT a palindrome number")
    else:
        if Input == Input[::-1]:
            print(Input + " is a palindrome")
        else:
            print(Input + " is NOT a palindrome")


palindrome()
