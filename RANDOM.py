import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='r!', description='Viewing reddit.')
bot.remove_command("help")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def help(ctx, *arg):
    author = ctx.message.author
    if len(arg) > 0:
        if arg[0].lower() == "nsfw":
            embed = discord.Embed(
                colour=discord.Colour.orange()
            )
            embed.set_author(name="NSFW Help")
            embed.add_field(name="r!hentai", value="return a random hentai image from r/hentai", inline=False)
            embed.add_field(name="r!butt", value="return a random butt image from r/butt ", inline=False)
            embed.add_field(name="r!feet", value="return a random feet image from r/feet ", inline=False)
            embed.add_field(name="r!porngif", value="return a random porn gif from r/porngifs ", inline=False)
            embed.add_field(name="r!r34", value="return a random image with the given arguments from rule34.xxx ", inline=False)
            embed.add_field(name="r!reddit", value="return a random post or image on the reddit of the given argument ", inline=False)

            await ctx.send(embed=embed)

        elif arg[0].lower() == "general":
            embed = discord.Embed(
                colour=discord.Colour.orange()
            )
            embed.set_author(name="General Help")

            await ctx.send(embed=embed)

        else:
            await ctx.send("the category "+arg[0]+" don't exist")
    else:
        embed = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name="General Help")
        embed.add_field(name="r!help nsfw", value="return a list of all the nsfw commands ", inline=False)
        embed.add_field(name="r!help general ", value="return a list of all the general commands ", inline=False)

        await ctx.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


token = open("token.txt","r").readline()
bot.run(token)