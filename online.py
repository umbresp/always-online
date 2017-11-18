import discord
from discord.ext import commands
import os

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix=!, self_bot=True, description="e")

@bot.command(pass_context=True)
async def ping(ctx):
    """Pong! Check your response time."""
    msgtime = ctx.message.timestamp.now()
    await (await bot.ws.ping())
    now = datetime.datetime.now()
    ping = now - msgtime
    pong = discord.Embed(title='Pong! Response Time:',
    					 description=str(ping.microseconds / 1000.0) + ' ms',
                         color=0x00ffff)
    await bot.say(embed=pong)
    
try:
    bot.run(TOKEN.strip('\"'), bot=False)
except Exception as e:
    print(f'\n[ERROR]: \n{e}\n')
