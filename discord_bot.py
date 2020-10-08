import discord
import json

global CONFIG

client = discord.Client()
token = ""

#import config file
with open('config.json', 'r') as f:
    getFile = json.load(f)
    global CONFIG
    CONFIG = getFile["services"]["discord"][0]

token = CONFIG["token"]

# bot start
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# bot get message
@client.event
async def on_message(message):
    # if get message for bot > return none
    if message.author.bot:
        return None

    if message.content.startswith('!Hi'):
        channel = message.channel
        await channel.send('Welcome!')

    if message.content.startswith('!Qadjoke'):
        channel = message.channel
        await channel.send('Welcome!')

client.run(token)