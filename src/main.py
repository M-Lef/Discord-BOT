from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 1  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('ping')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author.name)

@bot.command()
async def d6(ctx):
    await ctx.send(random.randrange(1, 6))

@bot.event
async def on_message(message):
    if message.content == 'Salut tout le monde':
        await message.channel.send('Salut tout seul')

    await bot.process_commands(message)

@bot.command()
async def admin(ctx, roleName):
    await ctx.guild.create_role(name="Admin", colour=discord.Colour(0x0062ff), permissions=discord.Permissions(8))

@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

@bot.command()
async def count(ctx):
    online = 0
    offline = 0
    idle = 0
    do_not_distrub = 0
    for user in ctx.guild.members:
        if str(user.status) == 'online' :
            online += 1
        if str(user.status) == 'offline' :
            offline += 1
        if str(user.status) == 'idle' :
            idle += 1
        if str(user.status) == 'dnd' :
            do_not_distrub += 1
    await ctx.send('online : ' + str(online) + '\noffline : ' + str(offline) + 
    '\nidle :  ' +  str(idle) + '\ndnd : ' +  str(do_not_distrub))

@bot.command()
async def count2(ctx):
    online=[]
    offline=[]
    idle=[]
    do_not_distrub=[]
    for user in ctx.guild.members:
        if str(user.status) == 'online' :
            online.append(user.name)
        if str(user.status) == 'offline' :
            offline.append(user.name)
        if str(user.status) == 'idle' :
            idle.append(user.name)
        if str(user.status) == 'dnd' :
            do_not_distrub.append(user.name)
    
    for user in online:
        await ctx.send(user + ' is online')
    for user in offline:
        await ctx.send(user + ' is offline')
    for user in idle:
        await ctx.send(user + ' is idle')
    for user in do_not_distrub:
        await ctx.send(user + ' is do_not_distrub')

@bot.command()
async def poll(ctx, msg):
    await ctx.send(msg)

token = ""
bot.run(token)  # Starts the bot
