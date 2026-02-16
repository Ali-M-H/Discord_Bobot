import discord
from discord.ext import commands
import requests
import secret_variables  as sv # This holds the variables "token" and "guild_id"

class Client(commands.Bot):
    async def on_ready(self):
        """prints in terminal when the bot starts working"""

        try: # Makes sure the commands work in my test server and says if all the commands work
            syncedGlobal = await self.tree.sync()
            print(f"synced {len(syncedGlobal)} commands Globally!!")
            
            guild = discord.Object(id=sv.guild_id)
            syncedGuild = await self.tree.sync(guild=GUILD_ID)
            print(f"synced {len(syncedGuild)} commands to guild {guild.id}!!")
            print(f"We are ready to rumble!!! {self.user}!!")


        except Exception as e: # Shows if errors show up
            print(f"Error syncing commands: {e}")


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix= "!", intents = intents)
GUILD_ID = discord.Object(id=sv.guild_id)



## / commands below

#-------------------------------------------------------------#
@client.tree.command(name="howo",description="giving a fabulous hello!")
async def hello(interaction: discord.Interaction):
    """says howo in the server using a / code"""
    await interaction.response.send_message("Howo")
#-------------------------------------------------------------#


#-------------------------------------------------------------

@client.tree.command(name="echo",description="Echo echo echo")
async def echo(interaction: discord.Interaction,printer:str):
    """Takes a message and sends it out through the bot"""
    await interaction.response.send_message(printer)
#-------------------------------------------------------------#



#-------------------------------------------------------------#

@client.tree.command(name="r", description="Rolls XdY dice + N")
async def r(interaction: discord.Interaction,dice:str):
    """Takes 3 possible numbers to roll X number of Y dice and add N to the total"""
    rolls = hf.roll(interaction,dice)

    if rolls == "Value Error":
        await interaction.response.send_message("Value Error in rolling")
        return



    if len(rolls[2]) == 1:
        rolls[2] = rolls[2][0]

    if rolls[0] == 0:
        await interaction.response.send_message(
        f"**`{dice}`** was rolled into **`{rolls[2]}`** \n Equaling: **`{rolls[1]}`**")
    else:
        await interaction.response.send_message(f"**`{dice}`** was rolled into **`{rolls[2]}`** + **`{rolls[0]}`** \n Equaling: **`{rolls[1]}`**")


#-------------------------------------------------------------#




#-------------------------------------------------------------#

@client.tree.command(name="dadjoke", description="Gives a random dadjoke")
async def dadjoke(interaction: discord.Interaction):
    """Gets a joke from the "https://icanhazdadjoke.com" API and sends it as a message"""
    url = "https://icanhazdadjoke.com"
    joke = requests.get(url, headers={"Accept" : "application/json"})
    await interaction.response.send_message(joke.json()["joke"])

#-------------------------------------------------------------#





client.run(sv.token)
