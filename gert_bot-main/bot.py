import discord
from discord.ext import commands
import json



@bot.event
async def on_ready():
    print(">>Bot is online <<")


@bot.command()
async def ping(ctx): 
    await ctx.send(f'{bot.latency*1000}(ms)')

@bot.command()
async def 圖片(ctx):
    pic=('https://tenor.com/view/dog-turn-table-gif-15526139')
    await ctx.send(pic)
@bot.command()
async def 黑人(ctx):
    pict=('https://tenor.com/view/gawr-gura-gawr-gura-kanye-kanye-kanye-west-hololive-gif-19498253')
    await ctx.send(pict)
@bot.command()
async def 樺木是甚麼(ctx):
    await ctx.send('低能兒')
bot.run(jdata['token'])