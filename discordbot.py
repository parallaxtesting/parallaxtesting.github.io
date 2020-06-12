import discord
from discord.ext import commands
import botkey

client = commands.Bot(command_prefix = '+')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message_delete(message):
    channel = client.get_channel(718943548795387955)
    await channel.send('```ini\n[Deleted]\n    [{0}]\n    [{1}]\n    [{2}]```'.format(message.channel.name, message.author.name, message.content))
    print("DELETED", message.channel.name, message.author, message.content, sep=': ')

@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return
    channel = client.get_channel(718943548795387955)
    await channel.send('```yaml\n[Edited]\n    [{0}]\n    [{1}]\n    [{2}]\n    [{3}]```'.format(before.channel.name, before.author.name, before.content, after.content))
    print("EDITED", before.channel.name, before.author, before.content, after.content, sep=': ')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any([keyword in message.content for keyword in ('Fag','fag', 'Faggot', 'faggot', 'Nig', 'nig', 'nigger', 'nigga', 'Retard', 'retard')]):
        channel = client.get_channel(718943548795387955)
        await channel.send('```css\n[Alert]\n    [{0}]\n    [{1}]\n    [{2}]```'.format(message.channel.name, message.author.name, message.content))
        print("ALERT", message.channel.name, message.author, message.content, sep=': ')
    await client.process_commands(message)
    
@client.event
async def on_member_join(member):
    print('Member Joined'.format(client))
    channel = client.get_channel(709473570446639227)
    primary = client.get_channel(705812649299935283)
    secondary = client.get_channel(709464646066634844)
    rules = client.get_channel(709477005250265088)
    welcome = client.get_channel(709473230863335474)
    await channel.send('{0} Thanks for joining our Valorant Discord server! Please be sure to react with your primary agent in the {1} channel and your most played secondary agent in the {2} channel. Don\'t forget to read over the {3} and {4} channel and respect all members of our server. Welcome to The Valorous Ones!'.format(member.mention, primary.mention, secondary.mention, rules.mention, welcome.mention))

@client.command()
async def embed(message):
    embed = discord.Embed(title="Sorry, that's an admin-only command :(", color=0xe6254e) #, description="Desc"
    channel = message.channel
        #embed.add_field(name="Field1", value="hi", inline=False)
        #embed.add_field(name="Field2", value="hi2", inline=False)
    await channel.send(embed=embed)

@client.command()
async def status(message, arg1):
    if message.author.id == 240269038977024000:
        await client.change_presence(activity=discord.Game(name="Version {0}".format(arg1)))
    else:
        embed = discord.Embed(title="Sorry, that's a developer command :(", color=0xe6254e)
        channel = message.channel     
        await channel.send(embed=embed)

@client.command()
async def twitter(message):
    channel = message.channel
    await channel.send('https://twitter.com/PlayVALORANT/status/1270885607443582977')
    
@client.command()
async def hi(message):
    channel = message.channel
    await channel.send('Hello, {0} :)'.format(message.author.mention))

client.run(botkey.TOKEN)