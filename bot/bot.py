import discord
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Boss data JSON
with open(r'C:\haha fy\projects\jarhead\backend\bosess.json', 'r') as file:
    boss_data = json.load(file)

@client.event
async def on_ready():
    print('Jarhead jacked in')

@client.event
# Message Listener:
async def on_message(message):
    if message.author == client.user:
        return
    
    # Bot intro:
    if message.content.startswith('!jarhead'):
        description = "I'm Jarhead, your very own Elden Ring companion. You can ask me about different aspects of the game and track the progress of your playthrough.\n\n"
        description += "**!bosses** - Gather info about different bosses.\n"
        description += "**!weapons** - Explore various weapons and weapon types.\n"
        description += "**!spells** - Learn about different spells.\n"
        description += "**!incantations** - Check out these incantations.\n"
        description += "**!flasks** - Discover which physick combo works the best.\n"
        description += "**!armour** - Look dapper on your adventure."

        embed = discord.Embed(
            title="Greetings Tarnished",
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/NxGINpp.png')

        await message.channel.send(embed=embed)
        
    # Boss command:
    elif message.content.startswith('!bosses'):
        query = message.content.split(' ', 1)
        if len(query) == 1:
            overworld_locations = []
            underworld_locations = []

            for location, data in boss_data.items():
                if location.lower() in ['overworld', 'underworld']:
                    continue
                if "contents" in data:
                    if location.lower() in ['limgrave', 'weeping peninsula', 'liurnia of the lakes', 'moonlight altar', 'caelid', 'dragonbarrow', 'altus plateau', 'capital outskirts', 'leyndell, royal capital', 'mt. gelmir', 'forbidden lands', 'mountaintops of the giants', 'consecrated snowfield', 'miquella\'s haligtree', 'crumbling farum azula']:
                        overworld_locations.append(location)
                    else:
                        underworld_locations.append(location)

            overworld_locations.sort()
            underworld_locations.sort()

            description = "Welcome to the Boss Catalogue. \nSimply use the command !bosses `location` with your desired location, and I will promptly provide you with information.\n\n"
            description += "**Overworld:**\n"
            description += '\n'.join(overworld_locations) + "\n\n"
            description += "**Underworld:**\n"
            description += '\n'.join(underworld_locations)

            title = "Bosses" 

        else:
            location_query = query[1].strip().title()
            location = None

            for key in boss_data.keys():
                if location_query.lower() in key.lower():
                    location = key
                    break

            if location is not None:
                description = '\n'.join(boss_data[location]['contents'])
                title = f"Bosses in {location}:"
            else:
                description = f"Sorry, I couldn't find information for {location_query}."
                title = "Bosses"

        embed = discord.Embed(
            title=title, 
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/yf9ImzL.png')
        await message.channel.send(embed=embed)

client.run('MTE2ODQ5NTEzNTcyNjc2ODEyOA.G7BcBX.LXKSjxyusWXx1tahcnMVLKBZII3coUjOGu7WgI')