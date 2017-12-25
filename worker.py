import discord
from discord.ext import commands

import json
import urllib.request

TOKEN = 'Mzk0OTQ4MjE0MDY5MTMzMzE1.DSLv-w.6UUj_DbgHpY44dCmuSLnZYMPZrE'

description = '''Coinbot in Python'''
bot = commands.Bot(command_prefix = '?', description = description)

@bot.event
async def on_ready():
    print('Login Info')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def coin(sym : str):
    """Gets the coin info"""
    coinData = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/?convert=USD&limit=1200").read()
    coinData = coinData.decode('utf-8')
    data = json.loads(coinData)
    ## No replacement necessary since we can load string directly into JSON format
    ##coinData = coinData.decode('utf8').replace("'",'"')
    ##print(coinData)

    flag = False

    for x in range(0, 1200):
        ##print(data[x]["id"])
        if data[x]["symbol"] == sym:
            flag = True
            await bot.say("Name: " + data[x]["name"] + " | " + "Rank: " + data[x]["rank"] + "\n"
            + "Symbol: " + data[x]["symbol"] + "\n" 
            + "Price (USD): " + data[x]["price_usd"] + "\n"
            + "Price (BTC): " + data[x]["price_btc"] + "\n"
            + "% Change 1 HR: " + data[x]["percent_change_1h"] + "%\n"
            + "% Change 24 HR: " + data[x]["percent_change_24h"] + "%\n"
            + "% Change 7 Days: " + data[x]["percent_change_7d"] + "%\n")
         
            return

    if flag == False:
        await bot.say(sym + " was not found in the crypto-market.")

bot.run(TOKEN)
