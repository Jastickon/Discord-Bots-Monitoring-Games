import requests
import threading
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio

TOKEN = "" # Ввидите токен вашего бота
ip = "insquad.gta5rp.com:22005" # Ввидите IP Вашего сервера


bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

def getPlayers(ip:str) -> tuple:
    """

    :param ip: "insquad.gta5rp.com:22005" or "8.8.8.8:8080"
    :return: (cur_player | max | peak)
    """
    s = requests.get("https://cdn.rage.mp/master")
    data = s.content
    conData = eval(data)
    for i in conData:
        if i == ip:
            data =conData[i]
            return data['players'],data['maxplayers']

players=None
async def online1():
    global players
    while True:
        try:
            time.sleep(10)
            cur,maxx = getPlayers(ip)
            player_count = f"{cur}/{maxx}"
            print(f"Данные обновлены до значения {player_count}")
            players=player_count
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"онлайн {player_count}"))
        except:
            await bot.change_presence(status=discord.Status.do_not_disturb)
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
