import discord
from discord.ext import commands
from phlib import PornHub
import random
ph = PornHub()

client = commands.Bot(command_prefix = '.',description="Hello there!! I'm Audrey Bitoni")

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
        arg1 = random.choice(cat);
    a = (list)(ph.search(arg1,max=20))
    sample = random.choices(a,k=arg2)
    for i in sample:
        pp = f'{i.title}\n{i.url}'
        await ctx.channel.send(pp)

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

client.run('NzA2NDY5MTEzOTI0NjgxNzQ5.Xq7tLQ.7dzpIKx1jPK7ZTHj-rNb7ehoR1o')