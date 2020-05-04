import discord
from discord.ext import commands
from phlib import PornHub
import random
import json
import requests
ph = PornHub()

client = commands.Bot(command_prefix = '.',description="Hello there!! I'm Audrey Bitoni")
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.orange()
    )
    st = '''here are all the commands
    {use dot(.) as prefix before any command}
    **example**           **description**
    **.help**-----------> *to open this message*
    **.link**-----------> *gives random porn link*
    **.link gang-bang**--> *keyword should be separated by '-'(dash) not ' '(space)*
    **.degi**-----------> *some random reply from audrey bitoni*
    **.clear a**--------> *'a' is an integer it deletes last 'a' messages from chat*      
    **.info username**--> *shows rating and rank of username in codeforces*
    **.contest**--------> *to know codeforces upcoming contest timing*
    **.register**-------> *to get registration page link of the codeforces*
    **.poblem**---------> *gives random problem (from level A,B,C)*
    **.poblem  B**------> *gives problem from level B*
    **.poblem dp**------> *gives problem from tag dp (level A,B,C)*
    **.poblem dp E**----> *gives level E problem from tag dp*
    **.tags**-----------> *gives tag that has to used in .poblem*
    **.me_ghissu**------> *github code*

    **DESCLAIME - gaali mt dena agr bezti ni krani to**
    '''
    embed.set_author(name='help')
    embed.add_field(name="Hello There!!",value=st,inline=False)

    await ctx.send(st)


@client.command()
async def degi(ctx):
    list = ['Abay Saalee!!','Tu le skta hai to lele','abey saaand','ooo tauuu tham jaa','tum jaise ko choochi me dba lu me!!','and mand ka tola, tu BKL']
    await ctx.channel.send(random.choice(list))

@client.command()
async def link(ctx,arg1=None):
    cat = ph.categories
    if arg1 == None:
        arg1 = random.choice(cat).title
    arg1 = arg1.replace("-"," ")
    # print(arg1)
    a = (ph.search(arg1,max=10))
    print(arg1)
    a = (list)(a)
    sample = random.choice(a)
    embed = discord.Embed(
        colour = discord.Color.dark_purple()
    )
    
    pp = f'{sample.title}\n{sample.url}'
    embed.add_field(name=ctx.message.author,value=pp)
    # pp = "testing"
    await ctx.channel.send(embed=embed)

@client.command()
async def clear(ctx,amount=5):
    print(ctx.message.author.name)
    # if ctx.message.author != client.user:
    #     return
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):
    if message.author.name == 'Miss_Mooooo':
        return
    name = message.author.name
    test = name.split("#")
    # print(test[0])
    gali = ["Maderchod","Bhosadike","Bhen chod","Beti chod","bhadve","Chutiya",
    "Gaandu","lawde","landoore","choot ke bhoot","lavde ke baal","jhaat si sakal ke",
    "sadi hui gaand","randii","gend deti rend","chamak-landoore","chamkeele gaand","bhosdu-nandan",""]
    gali2 = ["chod","BC","bsdk","chut","gand","gaand","dalle","daale","choot","randi","rande","gend","saale","bhadv","bhadw","lavd","lawd","lund","chooch"]
    channel = message.channel
    embed = discord.Embed(
        colour = discord.Color.orange()

    )
    gg = message.content.upper()
    embed.set_author(name="Audrey")
    st = f"Sun bey {test[0]} ** {random.choice(gali)} ** \n\nChats saaf suthri rakh, aage se mt krio ye"
    embed.add_field(name='Satya Vachan:',value=st)
    for i in gali2:
        i=i.upper()
        if gg.find(i)!=-1:
            await channel.send(message.author,embed=embed)
            break

    await client.process_commands(message)

@client.command()
async def info(ctx,handle="please_enter_handle"):
    if handle=="please_enter_handle":
        await ctx.message.channel.send("Please type codeforces username along with command( .info username)")
        return
    channel = ctx.message.channel
    y = requests.get(f' https://codeforces.com/api/user.info?handles={handle}').json()
    if y['status']=='FAILED':
        await ctx.message.channel.send("Please enter valid username or may be codeforces is down")
        return
    x = y['result'][0]
    rating = x['rating']
    rank = x['rank']
    embed = discord.Embed(
        colour= discord.Color.orange(),
        title=f'{handle}'
    )
    inf = "Rating = {}, Rank = {}".format(rating,rank)
    embed.add_field(name=f'{handle}', value=inf)
    await channel.send(embed=embed)

@client.command()
async def contest(ctx):
    y = requests.get(f'https://codeforces.com/api/contest.list?gym=false').json()
    if y['status']=='FAILED':
        await ctx.channel.send("Looks like codeforces is down")
        return
    y = y['result']
    for i in y:
        if i['phase']=='BEFORE':
            st = -1*(int)(i['relativeTimeSeconds'])
            days = int(st/(3600*24))
            rem = st%(3600*24)
            hrs = int((rem)/3600)
            rem = rem%3600
            mins = int(rem/60)
            sec = int(rem%60)
            ans = time_dede(days,hrs,mins,sec,i['name'])
            await ctx.channel.send(ans)
        else:
            break

def time_dede(days,hrs,mins,sec,name):
    if days!=0:
        return f"**{name}** (*{days}days : {hrs}Hrs : {mins}mins : {sec}secs left*)"
    elif hrs!=0:
        return f"**{name}** (*{hrs}Hrs : {mins}mins : {sec}secs left*)"
    elif mins!=0:
        return f"**{name}** (*{mins}mins : {sec}secs left*)"
    else:
        return f"**{name}** (*{sec}secs left*)"
    
@client.command()
async def register(ctx):
    await ctx.channel.send("https://codeforces.com/contests")

@client.command()
async def tags(ctx):
    await ctx.channel.send(file=discord.File('tag.png'))

@client.command()
async def poblem(ctx,tag1=None,tag2=None):
    tag = ['2-sat', 'binary search', 'bitmasks', 'brute force', 'chinese remainder theorem', 
    'combinatorics', 'constructive algorithms', 'data structures', 'dfs and similar', 'divide and conquer', 
    'dp', 'dsu', 'expression parsing', 'fft', 'flows', 'games', 'geometry', 'graph matchings', 'graphs', 
    'greedy', 'hashing', 'implementation', 'interactive', 'math', 'matrices', 'meet-in-the-middle', 'number theory', 
    'probabilities', 'schedules', 'shortest paths', 'sortings', 'string suffix structures', 'strings', 'ternary search', 'trees', 'two pointers']

    if tag1==None:
        tag1 = random.choice(tag)
    if len(tag1)==1:
        tag2 = tag1
        tag1 = random.choice(tag)

    if tag2 == None:
        tag2 = random.choice(['a','b','c'])
    tag1 = tag1.replace("-"," ")
    print(tag1)
    tag2 = tag2.upper()
    z = requests.get(f'https://codeforces.com/api/problemset.problems?tags={tag1}').json()['result']['problems']
    ans = []
    for i in z:
        if i['index']==tag2:
            ans.append(i)
    if len(ans)!=0:
        sample = random.choice(ans)
        rating = sample['rating']
        prob = f"**rating = {rating}** \nhttps://codeforces.com/contest/{sample['contestId']}/problem/{sample['index']}"
        await ctx.channel.send(prob)
    else:
        await ctx.channel.send("bhai bhooot dhunda pr nhi mila\nye tags use kr\n aisa kuch")
        await ctx.channel.send(file=discord.File('tag.png'))

@client.command()
async def me_ghissu(ctx):
    name = ctx.message.author
    url = 'https://github.com/abhishekshakya?tab=repositories'
    s = f"ye le code ghissu\n{url}"
    await ctx.channel.send(s)





with open('config.json','r') as openfile:
    token = json.load(openfile)
token = token['token']
client.run(token)