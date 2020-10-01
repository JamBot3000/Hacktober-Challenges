const Discord = require('discord.js'); //Imports the discord js api

const botconfig = require("./bot-config.json") //Imports the json file containing the bot configuration properties

const client = new Discord.Client(); //Create the client

client.once('ready', () => { //When ready
    console.log('Bot is ready to recieve commands!'); //Print on the console this
});

client.on('message', message => { //When recieved a new message, get the message...
    let prefix = botconfig.prefix //Get the prefix from the configuration file
    switch (message.content) { //If the content of the message is
        case `${prefix}d20`: //!d20
            response( //Prepares a response for the bot to send
                message, //Get the channel that the comand was send and by which user
                "d20", //Which type of dice
                Math.trunc(Math.random() * 20) //get random number between 0 and 20
            )
            break;
        case `${prefix}d12`:
            response(message, "d12", Math.trunc(Math.random() * 12))//get random number between 0 and 12
            break;
        case `${prefix}d8`:
            response(message, "d8", Math.trunc(Math.random() * 8))//get random number between 0 and 8
            break;
        case `${prefix}d6`:
            response(message, "d6", Math.trunc(Math.random() * 6))//get random number between 0 and 6
            break;
        case `${prefix}d4`:
            response(message, "d4", Math.trunc(Math.random() * 4))//get random number between 0 and 4
            break;
        case `${prefix}coin`: //get heads or tails
            let coin = Math.trunc((Math.random() * 2)) % 2 
            //Gets random number, divide it by two and gets the remainder, it can be either 0 or 1
            if (coin == 1) { //if its one
                response(message, "coin", "heads") //Send heads
            } else {
                response(message, "coin", "tails")//Send tails
            }
            break;
        case `${prefix}help`: //If the message is the help command

            //Send all possible commands this bot can recieve with relevant info
            message.channel.send(`Hey ${message.author}! These are my comands`)
            message.channel.send(`comand pattern: ${prefix}[dice] (e.g: &d20 -> roll a 20 sided dice)`)
            message.channel.send(`&d20 &d12 &d8 &d6 &d4 &coin `)
            break;
    }
});

function response(message, dice, result) {
    console.log(message.author.username + " : " + dice + " : " + result)
    //Prints on the console where the bot is running
    //e.g: User#1234 : d20 : 1

    message.channel.send(`${message.username} you got ${result} on the ${dice}`)
    //Sends a message on the channel (where the comand was sent from)
    //the result pinging the user that sent the comand
    //e.g: User you got 1 on the d20
}

client.login(botconfig.token); //Logs in the bot on discord
