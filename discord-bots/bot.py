import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '"')

@client.event
async def on_ready():
	print('Bot is online!')

@client.command(aliases=['p'])
async def ping(msg):
	await msg.send(f"Pong! Took {round(client.latency * 1000)}ms to respond.")

@client.command(aliases=['funny', 'makemelaugh'])
async def joke(msg):
	jokes = ['Why did the chicken cross the road? To get to the other side!',
			 "Why can't blind people eat fish? Because it's sea-food!",
			 "What is the astronaut's favourite key on the keyboard? The space bar."]
	await msg.send(f"Here's your joke: {random.choice(jokes)}")

client.run('token')