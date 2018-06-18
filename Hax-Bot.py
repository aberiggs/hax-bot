import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "~") #Initialise client bot

@client.event 
async def on_ready():
    print("Hax-Bot Online") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "~clear":
        await client.purge_from(message.channel, limit=none, check=100, before=None, after=None, around=None)

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id= '318857865609871360')
    while not client.is_closed:
        counter += 1
        await client.purge_from(client.get_channel('318857865609871360'), limit=1000, check=None, before=None, after=None, around=None)
        await asyncio.sleep(86400) # task runs every 24 hours
      
client.loop.create_task(my_background_task())
client.run("") #Replace token with your bots token
