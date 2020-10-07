import random

question = input("Please enter a question: ")

magicNum = random.randint(1, 3)

if magicNum == 1:
    print("\nDefinitely")
elif magicNum == 2:
    print("\nMaybe")
else:
    print("Nope")

