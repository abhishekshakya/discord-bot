import discord
from discord.ext import commands
from phlib import PornHub
import random
ph = PornHub()

client = commands.Bot(command_prefix = '.',description="Hello there!! I'm Audrey Bitoni")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")



@client.command()
async def degi(ctx):
    list = ['Abay Saalee!!','Tu le skta hai to lele','abey saaand','ooo tauuu tham jaa','tum jaise ko choochi me dba lu me!!','and mand ka tola, tu BKL']
    await ctx.channel.send(random.choice(list))

@client.command()
async def link(ctx,arg1=None,arg2=1):
    cat = ['milf','babe','big ass','brazzers','naughty america','boobs','step sister','step mom']
    if arg1 == None:
        arg1 = random.choice(cat)
    a = (list)(ph.search(arg1,max=20))
    sample = random.choices(a,k=arg2)
    for i in sample:
        pp = f'{i.title}\n{i.url}'
        await ctx.channel.send(pp)

@client.command()
async def clear(ctx,amount=5):
    if ctx.message.author != client.user:
        return
    await ctx.channel.purge(limit=amount)



@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.orange()
    )
    st = '''here are the some commands


    {use dot(.) as prefix before any command}


    ".help" -> to open this message


    ".link a b" -> 'a' is one word and 'b' is an integer
                    it returns porn link related to keyword 'a'


    ".degi" -> some random reply from audrey bitoni
    '''
    embed.set_author(name='help')
    embed.add_field(name="Hello There!!",value=st,inline=False)

    await ctx.send(author,embed=embed)

@client.event
async def on_message(message):
    gali = ["Maderchod","Bhosadike","Bhen chod","Beti chod","bhadve","Chutiya",
    "Gaandu","lawde","landoore","choot ke bhoot","lavde ke baal","jhaat si sakal ke",
    "sadi hui gaand","randii","gend deti rend","chamak-landoore","chamkeele gaand","bhosdu-nandan",""]
    gali2 = ["chod","BC","bsdk","Bsdk","chut","gand","gaand","dalle","daale","choot","randi","rande","gend","saale","bhadv","bhadw","lavd","lawd","lund","chooch"]
    channel = message.channel
    embed = discord.Embed(
        colour = discord.Color.orange()

    )
    embed.set_author(name="Audrey")
    st = f"Sun bey \"{random.choice(gali)}\" \n\nChats saaf suthri rakh, aage se mt krio ye"
    embed.add_field(name='Satya Vachan:',value=st)
    for i in gali2:
        if message.content.find(i)!=-1:
            await channel.send(message.author,embed=embed)
            break

    await client.process_commands(message)

client.run('NzA2NDY5MTEzOTI0NjgxNzQ5.Xq7tLQ.7dzpIKx1jPK7ZTHj-rNb7ehoR1o')