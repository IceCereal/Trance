"""
	Trance. A bot developed for Elements, The Music Club.
	She has some commands that deal with:
		> voting
		> logging
		> converting links between platforms

	Date: 2019-Jun-15
"""
import discord
from discord.ext import commands

import asyncio

from datetime import datetime

from pathlib import Path
import os

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# List of Directories
dir_core = Path("core/")
dir_res = Path("res/")

# READ TOKEN
with open(dir_res / "meta" / "TOKEN", 'r') as TokenFObj:
	TOKEN = TokenFObj.read()

BOT_PREFIX = ('++')
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
	activity = discord.Game("Music")
	await bot.change_presence(activity = activity)

	# LOAD COGS
	cogsList = ['cogs.owner.owner', 'cogs.meetup.meetup']
	
	for cog in cogsList:
		print ("Loading:\t" + cog + "...")
		bot.load_extension(cog)

	print (str(bot.user), "is Ready")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	await bot.process_commands(message)

# RUN THE BOT
bot.run(TOKEN)

### NOTHING AFTER THIS WORKS