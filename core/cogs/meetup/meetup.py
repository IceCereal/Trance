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

	@commands.command(
		name = "start_meetup",
		alias = ["s"],
		brief = "start the meetup",
		usage = "start_meetup",
		enabled = True,
		description = "A complete controller for the meet-up. This command handles \
			everything from start to finish. 3 minute wait for submitting the \
			YouTube link, via DM.",
		hidden = True
	)
	@commands.has_role("Admin")
	async def start_meetup(self, ctx, theme : str):
		print ("Begin: Start-Meetup")

		title = "Meet-Up | Theme:\t" + theme
		description = "Hello everyone! Interested members who want to share their song for today's Meet-Up, please react with the 🎵 emoji."
		timeFieldName="Time Left"
		timeToWait = 25

		# Send Embed about instructions
		insEmbed = discord.Embed(title = title, description = description)
		insEmbed.add_field(name=timeFieldName, value=str(timeToWait)+" seconds")


		embedMessage = await ctx.channel.send(embed = insEmbed)
		await embedMessage.add_reaction('🎵')

		for timeIter in range(timeToWait, 1, -5):
			insEmbed = discord.Embed(title = title, description = description)
			insEmbed.add_field(name=timeFieldName, value= str(timeIter)+" seconds")
			await embedMessage.edit(embed=insEmbed)
			await sleep(5)

		insEmbed = discord.Embed(title = title, description = description)
		await embedMessage.edit(embed=insEmbed)

		insMsg = await ctx.channel.fetch_message(embedMessage.id)
		reactions = insMsg.reactions
		print (reactions)

		musicNoteReaction = None
		for reaction in reactions:
			if str(reaction) == '🎵':
				musicNoteReaction = reaction
				break

		return



def setup(bot):
	bot.add_cog(meetupCog(bot))