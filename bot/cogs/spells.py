import discord
from discord.ext import commands
import json

class SpellsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open(r'C:\haha fy\projects\jarhead\backend\spells.json', 'r') as file:
            self.spell_data = json.load(file)

    @commands.command(name='spells')
    async def spells(self, ctx, *, spell_type=None):
        if spell_type is None:
            spells_types = []
            
            for spell_type, data in self.spell_data.items():
                if "contents" in data:
                    spells_types.append(spell_type)
            
            description = "Welcome to the Spells Catalogue. \nSimply use the command !spells `type` with your desired spell type, and I will promptly provide you with information.\n\n"
            description += '\n'.join(spells_types) + "\n\n"
            title = "Spells"
            
        else:
            spell_query = spell_type.strip().title()
            spell_type = None

            for key in self.spell_data.keys():
                if spell_query.lower() in key.lower():
                    spell_type = key
                    break

            if spell_type is not None:
                description = '\n'.join(self.spell_data[spell_type]['contents'])
                title = f"{spell_type}"
            else:
                description = f"Sorry, I couldn't find information for {spell_query}."
                title = "Spell type not found"

        embed = discord.Embed(
            title=title,
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/jC6V4Dd.png')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(SpellsCog(client))
