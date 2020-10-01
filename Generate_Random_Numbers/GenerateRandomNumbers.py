import random

def generateRandomNumber():
    number = random.randint(0, 65000000000000000)
    return number

print(generateRandomNumber())