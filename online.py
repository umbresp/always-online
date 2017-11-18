import discord
from discord.ext import commands
import os

TOKEN = os.environ['TOKEN']

bot = commands.Bot(command_prefix="!", self_bot=True, description="e")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pong")
    
@bot.command(name='presence')
async def _set(Type,*,message=None):
    """Change your discord game/stream!"""
    if Type.lower() == 'stream':
        await bot.change_presence(game=discord.Game(name=message,type=1,url=f'https://www.twitch.tv/{message}'),status='online')
        await bot.say(f'Set presence to. `Streaming {message}`')
    elif Type.lower() == 'game':
        await bot.change_presence(game=discord.Game(name=message))
        await bot.say(f'Set presence to `Playing {message}`')
    elif Type.lower() == 'clear':
        await bot.change_presence(game=None)
        await bot.say('Cleared Presence')
    else:
        await bot.say('Usage: `.presence [game/stream/clear] [message]`')
    
try:
    bot.run(TOKEN.strip('\"'), bot=False)
except Exception as e:
    print(f'\n[ERROR]: \n{e}\n')
