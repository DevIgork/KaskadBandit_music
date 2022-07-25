from webserver import keep_alive
import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='!')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
TOKEN = 'OTk5MzUwMzE0MzU4NTQ2NDUy.G-21e8.0lg8SlEprRLrmcHM5tTD6GxFwuRk_0uf8PlA3c'
bot.run(TOKEN)
keep_alive()