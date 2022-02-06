import discord
from discord.commands import Option
from dotenv import dotenv_values
from utils.logging import log
# Load the env file
config = dotenv_values(".env")

# Initiate the PyCord Bot.
bot = discord.Bot()

@bot.event
async def on_ready():
    # Log to the user that we're signed in.
    log(4, f"We have logged in as {bot.user}")

@bot.slash_command(
    guild_ids=[config["GUILD_ID"]],
    description="Get information about a specified server!",
    )
async def serverlookup(
    ctx: discord.ApplicationContext,
    serverid: Option(str, "Server ID"),
    hide: Option(bool, "Hide message?")
):
    roles = []
    for role in ctx.author.roles:
        roles.append(role.name)
    if config["ROLE_NAME"] in roles:
        if hide == True:
            await ctx.respond(f"Looking up {serverid}!", ephemeral=True)
        else:
            await ctx.respond(f"Looking up {serverid}!")
    else:
        log(3, f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) attempt to run the Server Lookup command!")
        await ctx.respond(f"Sorry, {ctx.author.name}, but you don't have permission to run this command!", ephemeral=True)

bot.run(config["BOT_TOKEN"])
