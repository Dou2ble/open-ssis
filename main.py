import os

import hikari
import lightbulb
from dotenv import load_dotenv

import embeds
import utils

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
@lightbulb.command("help", "Lista över bottens kommandon.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.context) -> None:
    await ctx.respond(
        hikari.Embed(
            title="Commands:",
            description="""
            **/help** - Lista över bottens kommandon.
            **/ping** - Testa att botten är online.
            **/mat** - Se veckans matsedel.
            **/schema** - Se klassens schema.            
            """
            ))

# ping command
@bot.command
@lightbulb.command("ping", "Testa att botten är online.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.context) -> None:
    await ctx.respond(
        hikari.Embed(
            title="Pong!",
            description=":ping_pong:"
            ))

# food command
@bot.command
@lightbulb.command("mat", "Se veckans matsedel.")
@lightbulb.implements(lightbulb.SlashCommand)
async def mat(ctx: lightbulb.context) -> None:
    try:
        await ctx.respond(embeds.SCRAPING)

        await ctx.edit_last_response(
            hikari.Embed(
                title="Eatery Kista Nod",
                description=utils.scrape_eatery()
                ))
    except Exception as e:
        await ctx.respond(
            hikari.Embed(
                title="Error",
                description=str(e)
                ))

@bot.command
@lightbulb.option("klass", "klassen du vill se schemat från", modifier=lightbulb.OptionModifier.CONSUME_REST, required=True)
@lightbulb.command("schema", "Se klassens schema.")
@lightbulb.implements(lightbulb.SlashCommand)
async def schema(ctx: lightbulb.context) -> None:
    try:
        await ctx.respond(
            ctx.options.klass.upper() +
            "\n" +
            utils.fetch_schema(ctx.options.klass))

        await ctx.edit_last_response(hikari.Embed().set_author(
            name="Google Kalender",
            url=utils.scrape_schema(ctx.options.klass),
            icon="resources/google_calendar.png"
        ))

    except Exception as e:
        await ctx.respond(
            hikari.Embed(
                title="Error",
                description=str(e)
                ))





bot.run(activity=hikari.Activity(type=hikari.ActivityType.WATCHING, name="/help"))



