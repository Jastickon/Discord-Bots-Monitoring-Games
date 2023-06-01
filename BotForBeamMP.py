import json
import requests
from bs4 import BeautifulSoup
import threading
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio

TOKEN = "MTA5NjUxODk4MTk4MjEwNTYzMQ.Gx34Hv.xVubTVURc6zz2bX1HK4MsZmTVpInaQxgvVI8y4"  # Ввидите токен вашего бота

ip = "65.108.199.114"
port = "25657"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

players = None

def getPlayers(ip,port):
    s = requests.get("https://backend.beammp.com/servers-info")
    data = json.loads(s.content)
    for i in data:
        if i["ip"] == ip and i["port"] == port:
            print(i)
            return i["players"],i["maxplayers"]

async def online1():
    global players
    while True:
        try:
            time.sleep(20)
            n,m = getPlayers(ip,port)
            player_count = f"{n}/{m}"
            print(f"Данные обновлены до значения {player_count}")
            players = player_count
            await bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=f"онлайн {player_count}"))
        except:
            await bot.change_presence(activity=discord.Activity(name=f"Сервер выключен"),
                                      status=discord.Status.idle)
            time.sleep(10)
            print("Сервер выключен")


t = threading.Thread(target=asyncio.run, args=(online1(),))
t.start()

@tasks.loop(seconds=10.0)
async def slow_count():
    if players is None: return
    print(f'{bot.user.name} проверка обновления')


@bot.event
async def on_message(message):
    print(f'Получено сообщение! Отправитель: {message.author} Текст: {message.content}, Сервер: {message.guild}')


@bot.event
async def on_ready():
    slow_count.start()
    print(f'{bot.user} запустился и готов к работе!')


bot.run(TOKEN)
