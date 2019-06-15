"""
	A Cog for Owner
	Author: 
"""

import discord
from discord.ext import commands
from asyncio import sleep
from os import path, makedirs
from json import dump, load
from pathlib import Path as PathPL

class ownerCog(commands.Cog):
	def __init__(self, bot):
		print ("Loading Cog:\townerCog")
		self.bot = bot

def setup(bot):
	bot.add_cog(ownerCog(bot))