import discord
from discord.ext import commands
import json

class IncantationsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open(r'C:\haha fy\projects\jarhead\backend\incantations.json', 'r') as file:
            self.incantation_data = json.load(file)

    @commands.command(name='incantations')
    async def incantations(self, ctx, *, incantation_type=None):
        if incantation_type is None:
            incantations_types = []
            
            for incantation_type, data in self.incantation_data.items():
                if "contents" in data:
                    incantations_types.append(incantation_type)
            
            description = "Welcome to the Incantations Catalogue. \nSimply use the command !incantations `type` with your desired incantation type, and I will promptly provide you with information.\n\n"
            description += '\n'.join(incantations_types) + "\n\n"
            title = "Incantations"
            
        else:
            incantation_query = incantation_type.strip().title()
            incantation_type = None

            for key in self.incantation_data.keys():
                if incantation_query.lower() in key.lower():
                    incantation_type = key
                    break

            if incantation_type is not None:
                description = '\n'.join(self.incantation_data[incantation_type]['contents'])
                title = f"{incantation_type}"
            else:
                description = f"Sorry, I couldn't find information for {incantation_query}."
                title = "Incantation type not found"

        embed = discord.Embed(
            title=title,
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/MDyzgk4.png')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(IncantationsCog(client))
