import discord, os, keep_alive, asyncio, datetime, pytz

from discord.ext import tasks, commands

client = commands.Bot(

  command_prefix=':',

  self_bot=True

)

@client.event

async def on_connect():

  await client.change_presence(activity = discord.Streaming(name = "  • OPEN JASA ALL SA-MP✓ | • 100% NO SCAM✓ | • ORDER DM AJA OK✓ | • SUBSCRIBE MY CHANNEL YOUTUBE✓", url = "https://www.twitch.tv/omitgaming"))


keep_alive.keep_alive()

client.run(os.getenv("TOKEN"), bot=False)
