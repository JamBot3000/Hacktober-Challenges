import random

goAgain = True

while goAgain == True:
    randomNum = random.randint(0, 100)
    userGuess = input("\nPlease guess the number: ")
    
    if userGuess == str(randomNum):
        userGoAgain = input("\nYou guessed the number! Would you like to go again? (y/n)")

        if str(userGoAgain) == "y":
            goAgain = True
        else:
            goAgain = False
    else:
        print("You guessed wrong! Try again")
    
print("\nThanks for playing")