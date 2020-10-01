#A number guessing game
#we created 5 variables

secret_word = "5"
guess = "what the user guesses"
guess_count = 0 #tells the user number of guess he has
guess_limit = 3 #tells the user how many times he could guess
out_of_guesses = False

#out of guesses is a boolean, we set it to either true or
# false but for the sake of ths program we set it as false

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess number: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses You lose!")
else: print("you win")
