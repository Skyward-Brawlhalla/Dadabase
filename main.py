import discord
import os
from discord.ext import commands
from modules.claim import claim
from modules.check import check
from modules.ping import ping
from modules.keep_alive import keep_alive
from modules.configure_server import configure_server
from modules.ps4.ps4_add import ps4_add
from modules.ps4.ps4_list import ps4_list
from modules.ps4.ps4_remove import ps4_remove
from discord.ext.commands import has_permissions

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['d!'], intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name='ping')
async def say(ctx):
    await ping(ctx)


@commands.has_role("NO Verified ✔")
@bot.command(name='claim')
async def claim_command(ctx, brawlhalla_id):
    await claim(ctx, brawlhalla_id)


@commands.has_role("NO Verified ✔")
@bot.command(name='check')
async def check_command(ctx):
    await check(ctx)

@has_permissions(administrator=True)
@bot.command(name='ps4add')
async def ps4_add_command(ctx, brawlhalla_id, brawlhalla_name):
    await ps4_add(ctx, brawlhalla_id, brawlhalla_name)

@has_permissions(administrator=True)
@bot.command(name='ps4list', aliases=['ps4ls'])
async def ps4_list_command(ctx):
    await ps4_list(ctx) 

@has_permissions(administrator=True)
@bot.command(name='ps4remove', aliases=['ps4rm'])
async def ps4_remove_command(ctx, brawlhalla_id):
    await ps4_remove(ctx, brawlhalla_id)


@bot.command('configureserver')
async def configure_server_command(ctx):
    await configure_server(ctx)


@claim_command.error
async def claim_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('format your message like the following\n`' +
                       bot.command_prefix[0] + 'claim brawlhalla_id`')


#keep_alive()
#bot.run(os.environ['BOT_KEY'])
