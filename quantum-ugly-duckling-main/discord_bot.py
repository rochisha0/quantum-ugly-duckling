import discord
import json
import CloudDB
import nqrng

from cloudant.result import Result

global CONFIG

client = discord.Client()
token = ""

#import config file
with open('config.json', 'r') as f:
    getFile = json.load(f)
    global CONFIG
    CONFIG = getFile["services"]["discord"][0]

token = CONFIG["token"]

#db connect
global my_database
my_database = CloudDB.connect_db()

# bot start
@client.event
async def on_ready():
    print("Login")
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
        arrResult = Result(my_database.all_docs, include_docs=True)
        dbNum = my_database.doc_count()
        num1 = nqrng.random_number() % dbNum
        num2 = nqrng.random_number() % dbNum
        num = (num1 * num2) % dbNum
        result = arrResult[num][0]['doc']['Qdad']
        print(f"{num} is randnum, result is {result}")
        await channel.send(f'{result}')

client.run(token)
