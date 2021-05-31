# Objectiv : learn to do a Discord bot
# Form : https://hackernoon.com/building-your-own-discord-bot-with-python-is-easy-pcn34w1

from discord_bot_maker import DBot

with open('discordtoken.txt') as f:
    TOKEN = f.read()

d = DBot(TOKEN)

d.createCommand(trigger = "jump", reply = "whoop!", reply2 = "I just jumped", emoji = "😄", image = "https://media.giphy.com/media/LzqKqSr1rs5Hi/giphy.gif", help = "jumps")

d()