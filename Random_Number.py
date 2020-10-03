import random

length=int(input('Enter Length of Random Number: '))
number=list('1234567890')
randnum=''
for i in range(length):
    randnum+=random.choice(number)
print(randnum)
