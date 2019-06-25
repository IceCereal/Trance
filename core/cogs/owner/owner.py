"""
	A Cog for Owner
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

	@commands.command(
		name = "logout",
		brief = "Log the client out",
		usage = "logout",
		enabled = True,
		description = "Log the client out. This is only an owner command.",
		hidden = True
	)
	@commands.is_owner()
	async def logout(self, ctx):
		print ("Logout - Initiated")
		await ctx.channel.send(content="Logout Sequence Initiated")

		#Any clean-up code goes here
		await self.bot.change_presence(status = discord.Status.offline)

		print ("Logout - Completed")
		await ctx.channel.send(content="Logout Sequence Completed")

		await sleep(1)
		await self.bot.logout()

def setup(bot):
	bot.add_cog(ownerCog(bot))