import discord  
from discord.ext import commands 
import music    
import help_cog 

cogs = [music]
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
bot.remove_command('help')

for i in range(len(cogs)):
    cogs[i].setup(bot)

TOKEN = "PUT YOUR TOKEN HERE"
bot.add_cog(help_cog(bot))
bot.run(TOKEN)

