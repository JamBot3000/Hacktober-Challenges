import discord
from discord.ext import commands
import discord.utils







TOKEN = ''
client = discord.Client()
client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command(name='infobot', description="infobot command")
@commands.guild_only()
async def infobot(self, ctx):
    embed = discord.Embed(title="INFO BOT", color=0x00e1ff)
    embed.add_field(name=str("GUILDS"),
                    value=f'`{len(client.guilds)}`',
                    inline=False)
    embed.add_field(name=str("LATENCY"),
                    value=f'`{round(client.latency * 1000)} ms`',
                    inline=False)
    embed.add_field(name=str("Total Commands"),
                    value=f'`{len(client.commands)}`',
                    inline=False)
    await ctx.send(embed=embed)

client.run(TOKEN, reconnect=True)

