require('dotenv').config()
const discord = require('discord.js');

const bot = new discord.Client();
const PREFIX = "--"

const COMMANDS = {
    ping:(msg, args)=>{
        msg.reply("pong!")
    },
    random:(msg, args)=>{
        let maxN;
        const DEFAULT = 100;
        if(args.length){
            try{
                maxN = parseInt(args[0]);
            }catch(e){
                maxN = DEFAULT;
            }
        }else{
            maxN = DEFAULT;
        }
        const randVal = Math.floor(Math.random() * maxN);
        msg.reply(" I picked " + randVal)
    }
}

function handleMessage(msg) {
    if(msg.author.client.bot){
        return;
    }
    if(!msg.content.startsWith(PREFIX)){
        return;
    }
    const trimContent = msg.content.substring(PREFIX.length);
    const args = trimContent.split(/[\t\n ]+/gi);
    const commandName = args.shift();
    console.log(args, ' ', commandName)
    if(!Object.keys(COMMANDS).includes(commandName)){
        return msg.reply("invalid command!");
    }
    COMMANDS[commandName](msg, args);
} 

bot.on('message', handleMessage)
bot.on('ready', ()=>{
    console.log('Bot single, and ready to mingle!');
    console.log(`Add me here: https://discord.com/api/oauth2/authorize?client_id=${bot.user.id}&permissions=11328&scope=bot`);
})

bot.login(process.env.DISCORD_TOKEN);
