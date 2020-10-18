import random

def my_decorator(func):
    def wrapper():
        print("The answer to you'r question is:")
        func()
    return wrapper

question = input("Please enter a question: ")

@my_decorator
def magic8():

    magicNum = random.randint(1, 5)

    if magicNum == 1:
        print("\nDefinitely")
    elif magicNum == 2:
        print("\nMaybe")
    elif magicNum == 3:
        print("Better not tell you now")
    elif magicNum == 4:
        print("My sources say no")
    else:
        print("Nope")

magic8()
