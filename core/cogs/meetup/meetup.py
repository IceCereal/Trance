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
	async def start_meetup(self, ctx, theme : str = None):

		if theme == None:
			theme = "Unknown"


		print ("Begin: Start-Meetup")

		title = "Meet-Up | Theme: " + theme
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
		await embedMessage.edit(embed=insEmbed, delete_after = 10)

		insMsg = await ctx.channel.fetch_message(embedMessage.id)
		reactions = insMsg.reactions
		print (reactions)

		musicNoteReaction = None
		for reaction in reactions:
			if str(reaction) == '🎵':
				musicNoteReaction = reaction
				break

		userPool = []
		async for user in musicNoteReaction.users():
			if user == self.bot.user:
				continue
			userPool.append(user)

		contendersEmbed = discord.Embed(title = "Meet-Up | Theme: "+theme+" | Contenders")

		for i in range(len(userPool)):
			contendersEmbed.add_field(name = str(i+1), value = str(userPool[i]))

		await ctx.channel.send(embed=contendersEmbed)

		guild = ctx.guild

		# Create the send link embed
		dm_start_Embed = discord.Embed(title = "Meet-Up | Theme: "+theme+" | Instructions")
		dm_start_Embed.add_field(name="1.", value="Please send a YouTube link of the song you would like to send that conforms to the theme of today's Meet-Up.")
		dm_start_Embed.add_field(name="2.", value="You have 2 minutes from the time of this message being sent to send the link.")
		# dm_start_Embed.add_field(name="3.", value="If another contender has sent the same link, you will be given an extra minute to send another link.")

		# TODO: Finish This
		# dmMessages_Start = []
		# for user in userPool:



		return



def setup(bot):
	bot.add_cog(meetupCog(bot))