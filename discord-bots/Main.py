# Packages.
## Packages default to Python.
import time

## Packages that have to be installed through the package manager.
import discord
from discord.ext import commands

bot = commands.AutoShardedBot(command_prefix = "!", case_insensitive = True)

@bot.command(aliases = "latency")
async def ping(ctx):
    """Get the latency between our bot and Discord as well as the latency of the host."""

    # Get the time at one point, trigger typing, get the time again then subtract the two values to get the host latency. To get API latency use self.bot.latency, get round trip by adding up the two latencies.
    t1 = time.perf_counter()
    await ctx.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(
        title = "🏓 Pong!",
        description = f"Host latency is { round((t2 - t1) * 1000) }ms.\nAPI latency is { int(round(self.bot.latency * 1000, 2)) }ms.\nRound Trip took { int(round((t2 - t1) * 1000) + round(self.bot.latency * 1000, 2)) }ms.",
    )
    await ctx.send(embed = embed)

@bot.event
async def on_shard_ready(shard_id):
    """When a shard starts print out that the shard has started.

    Args:
        shard_id (int): The ID of the shard that has started. (Starts from 0).
    """
    print(f"{Style.BRIGHT}{Fore.CYAN}[SHARD-STARTED]{Fore.WHITE} Shard {Fore.YELLOW}{shard_id}{Fore.WHITE} has started!")

@bot.event
async def on_ready():
    """When the bot fully starts print out that the bot has started and set the status."""
    print(f"[BOT-STARTED] I'm currently in {len(bot.guilds)} servers with {len(bot.users)} users!")
    await bot.change_presence(status = discord.Status.dnd, activity = discord.Game(f"with !help"))

# Start the bot.
bot.run("TOKEN")