import discord
from discord.ext import commands
import json

class BossCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open(r'C:\haha fy\projects\jarhead\backend\bosses.json', 'r') as file:
            self.boss_data = json.load(file)

    @commands.command(name='bosses')
    async def bosses(self, ctx, location=None):
        if location is None:
            overworld_locations = []
            underworld_locations = []

            for location, data in self.boss_data.items():
                if "contents" in data:
                    if location.lower() in ['limgrave', 'weeping peninsula', 'liurnia of the lakes', 'moonlight altar', 'caelid', 'dragonbarrow', 'altus plateau', 'capital outskirts', 'leyndell, royal capital', 'mt. gelmir', 'forbidden lands', 'mountaintops of the giants', 'consecrated snowfield', 'miquella\'s haligtree', 'crumbling farum azula']:
                        overworld_locations.append(location)
                    else:
                        underworld_locations.append(location)

            description = "Welcome to the Boss Catalogue. \nSimply use the command !bosses `location` with your desired location, and I will promptly provide you with information.\n\n"
            description += "**Overworld:**\n"
            description += '\n'.join(overworld_locations) + "\n\n"
            description += "**Underworld:**\n"
            description += '\n'.join(underworld_locations)
            title = "Bosses"

        else:
            location_query = location.strip().title()
            location = None

            for key in self.boss_data.keys():
                if location_query.lower() in key.lower():
                    location = key
                    break

            if location is not None:
                description = '\n'.join(self.boss_data[location]['contents'])
                title = f"Bosses in {location}:"
            else:
                description = f"Sorry, I couldn't find information for {location_query}."
                title = "Location not found"

        embed = discord.Embed(
            title=title,
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/yf9ImzL.png')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(BossCog(client))