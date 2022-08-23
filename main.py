#ssis discord bot

#import .env
from dotenv import load_dotenv
import os
import hikari
import lightbulb
import eatery

#load .env
load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = "!"

bot = lightbulb.BotApp(
    TOKEN,
    PREFIX,
    help_class=None,
    default_enabled_guilds=(
        580384337044701185, # test server
        1009416096891289651 # SSIS TE22B
        )
    )

# help command
@bot.command
@lightbulb.command("help", "Get a list of availible commands")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.context) -> None:
    await ctx.respond(
        hikari.Embed(
            title="Commands:",
            description="""
            **/help** - Get this link
            **/ping** - Check if the bot is online
            **/food** - Check the lunch menu for the week
            """
            ))

# ping command
@bot.command
@lightbulb.command("ping", "Ping the bot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.context) -> None:
    await ctx.respond(
        hikari.Embed(
            title="Pong!",
            description=":ping_pong:"
            ))

# food command
@bot.command
@lightbulb.command("food", "Get the food for the day.")
@lightbulb.implements(lightbulb.SlashCommand)
async def food(ctx: lightbulb.context) -> None:
    try:
        await ctx.respond("Scraping :hourglass:")

        await ctx.respond(
            hikari.Embed(
                title="Eatery Kista Nod",
                description=eatery.scrape()
                ))
    except Exception as e:
        await ctx.respond(
            hikari.Embed(
                title="Error",
                description=str(e)
                ))





bot.run(activity=hikari.Activity(type=hikari.ActivityType.WATCHING, name="/help"))



