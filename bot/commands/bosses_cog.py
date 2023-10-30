import discord
from discord.ext import commands
import json

class BossesCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Load boss data from the JSON file with the correct absolute file path
        with open(r'C:\haha fy\projects\jarhead\backend\bosess.json', 'r') as file:
            self.boss_data = json.load(file)

    @commands.command(name="bosses")
    async def list_bosses(self, ctx, location=None):
        if location is None:
            # Display all region names sorted under "Overworld" and "Underworld"
            overworld_locations = []
            underworld_locations = []

            for location, data in self.boss_data.items():
                if location.lower() in ['overworld', 'underworld']:
                    continue  # Skip these categories
                if "contents" in data:
                    if location.lower() in ['limgrave', 'weeping peninsula', 'liurnia of the lakes', 'moonlight altar', 'caelid', 'dragonbarrow', 'altus plateau', 'capital outskirts', 'leyndell, royal capital', 'mt. gelmir', 'forbidden lands', 'mountaintops of the giants', 'consecrated snowfield', 'miquella\'s haligtree', 'crumbling farum azula']:
                        overworld_locations.append(location)
                    else:
                        underworld_locations.append(location)

            overworld_locations.sort()
            underworld_locations.sort()

            description = "Welcome to the Boss Catalogue. Simply click on your desired location and boss, and I will promptly provide you with information about them.\n\n"
            description += "**Overworld:**\n"
            description += '\n'.join(overworld_locations) + "\n\n"
            description += "**Underworld:**\n"
            description += '\n'.join(underworld_locations)

            title = "Bosses"  # Set the title to "Bosses"
        else:
            # Display bosses for the specified location
            location_query = location.strip().title()
            location = None

            # Case-insensitive search for the location
            for key in self.boss_data.keys():
                if location_query.lower() in key.lower():
                    location = key
                    break

            if location is not None:
                description = '\n'.join(self.boss_data[location]['contents'])
                title = f"Bosses in {location}:"  # Set the title based on the location
            else:
                description = f"Sorry, I couldn't find information for {location_query}."
                title = "Bosses"

        embed = discord.Embed(
            title=title,  # Use the specified title
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/yf9ImzL.png')

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(BossesCog(client))