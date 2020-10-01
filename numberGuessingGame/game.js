const prompt = require("prompt-sync")() //Imports the comunications between the prompt

//Welcomes the player
console.log("Welcome to my number guessing game!!")

//Shows the player the rules
console.log("You have to guess a number between 1 and 100")

//How many tries the player has
var tries = Number(//Transforms it into a number
    prompt("How many tries do you want to have? ") //Gets an input from the user
)
while (isNaN(tries)) { //if the user writes something that isnt a number
    tries = Number(prompt("How many tries do you want to have? ")) //Get the input again
    if (isNaN(tries)) {
        console.log("Type a number!") //Shows the player what to do
        continue //restart the loop
    }
    break
}

let num = Math.trunc(Math.random() * 100) //Get a random number between 0 and 100
if (num == 0) num = 1 //If the random number is 0, turn it into a 1

while (tries > 0) {//While the player has tries
    console.log(`You have ${tries} try(ies)`) //Show the player how many tries
    let guess = Number(prompt("Guess the number! ")) //Ask for a number
    if (guess == NaN) { //If its not a number
        console.log("Type a number!") //Show the player what to do
        continue //Restart the loop
    }
    if (guess > num) { //If the guess is bigger than the number
        console.log("The number is smaller than your guess!") //Show to the player why his guess was wrong
        tries-- //Subtract by 1 his tries
    }
    else if (guess < num) { //If the guess is smaller than the numer
        console.log("The number is bigger than your guess!") //Show to the player why his guess was wrong
        tries-- //Subtract by 1 his tries
    }
    else { //By process of elimination, the guess is equals to the number
        console.log("Your guess was right number! Congratulations!") //Show the player that he got it right
        break //End the
    }
}