import discord
from discord.ext import commands
import json

class AshesCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open(r'C:\haha fy\projects\jarhead\backend\ashes.json', 'r') as file:
            self.ash_data = json.load(file)

    @commands.command(name='ashes')
    async def ashes(self, ctx, ash=None):
        if ash is None:
            ashes = []
            
            for ash, data in self.ash_data.items():
                if "contents" in data:
                    ashes.append(ash)
            
            description = "Welcome to the Ashes of War Catalogue. \nSimply use the command !ashes `type` with your desired ash type, and I will promptly provide you with information.\n\n"
            description += '\n'.join(ashes) + "\n\n"
            title = "Ashes of War"
            
        else:
            ash_query = ash.strip().title()
            ash = None

            for key in self.ash_data.keys():
                if ash_query.lower() in key.lower():
                    ash = key
                    break

            if ash is not None:
                description = '\n'.join(self.ash_data[ash]['contents'])
                title = f"{ash}"
            else:
                description = f"Sorry, I couldn't find information for {ash_query}."
                title = "Ash type not found"

        embed = discord.Embed(
            title=title,
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/QhDre6a.png')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(AshesCog(client))
