"""
	A driver Cog for the main purpose of Trance.
	It is to be executed during the meet-ups.
"""

import discord
from discord.ext import commands
from asyncio import sleep
from os import path, makedirs
from json import dump, load
from pathlib import Path as PathPL

class meetupCog(commands.Cog):
	def __init__(self, bot):
		print ("Loading Cog:\tmeetupCog")
		self.bot = bot

def setup(bot):
	bot.add_cog(meetupCog(bot))