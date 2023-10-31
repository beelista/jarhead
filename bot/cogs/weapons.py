import discord
from discord.ext import commands
import json

class WeaponsCog(commands.Cog):
    def __init__(self, client):
        self.client = client

        with open(r'C:\haha fy\projects\jarhead\backend\weapons.json', 'r') as file:
            self.weapon_data = json.load(file)

    @commands.command(name='weapons')
    async def weapons(self, ctx, *, weapon_type=None):
        if weapon_type is None:
            weapons_types = []
            
            for weapon_type, data in self.weapon_data.items():
                if "contents" in data:
                    weapons_types.append(weapon_type)
            
            description = "Welcome to the Weapons Catalogue. \nSimply use the command !weapons `type` with your desired weapon type, and I will promptly provide you with information.\n\n"
            description += '\n'.join(weapons_types) + "\n\n"
            title = "Weapons"
            
        else:
            weapon_query = weapon_type.strip().title()
            weapon_type = None

            for key in self.weapon_data.keys():
                if weapon_query.lower() in key.lower():
                    weapon_type = key
                    break

            if weapon_type is not None:
                description = '\n'.join(self.weapon_data[weapon_type]['contents'])
                title = f"{weapon_type}"
            else:
                description = f"Sorry, I couldn't find information for {weapon_query}."
                title = "Weapon type not found"

        embed = discord.Embed(
            title=title,
            description=description,
            color=0xFFE467
        )

        embed.set_thumbnail(url='https://i.imgur.com/Ffbgmfy.png')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(WeaponsCog(client))
