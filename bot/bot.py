import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('Jarhead jacked in')
    await client.load_extension('cogs.bosses')
    await client.load_extension('cogs.weapons')
    await client.load_extension('cogs.ashes')

@client.command(name='jarhead')
async def jarhead(ctx):
    description = "I'm Jarhead, your very own Elden Ring companion. You can ask me about different aspects of the game and track the progress of your playthrough.\n\n"
    description += "**!bosses** - Gather info about different bosses.\n"
    description += "**!weapons** - Explore various weapons and weapon types.\n"
    description += "**!ashes** - See the Ashes of War available to you.\n"
    description += "**!talismans** - Try out what talismans suit your build the best.\n"
    description += "**!spells** - Learn about different spells.\n"
    description += "**!incantations** - Check out these incantations.\n"
    description += "**!flasks** - Discover all Golden Seed, Sacred Tear and Physick Tear locations.\n"
    description += "**!armour** - Look dapper on your adventure."

    embed = discord.Embed(
        title="Greetings Tarnished",
        description=description,
        color=0xFFE467
    )

    embed.set_thumbnail(url='https://i.imgur.com/NxGINpp.png')

    await ctx.send(embed=embed)

client.run('cant be leaking that')