import requests
from bs4 import BeautifulSoup
import threading
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio

TOKEN = "" # Ввидите токен вашего бота
IP = "46.174.53.204:27015" # Ввидите ваш IP

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

players=None
async def online1():
    global players
    while True:
        try:
            time.sleep(20)
            url = "https://tsarvar.com/ru/servers/garrys-mod/" + IP
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            online = soup.find_all('span', class_='srvPage-countCur')[0].text
            playermax = soup.find_all('span', class_='srvPage-countMax')[0].text
            player_count=(f"{online}/{playermax}")
            print(f"Данные обновлены до значения {player_count}")
            players=player_count
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"онлайн {player_count}"))
        except:
            await bot.change_presence(activity=discord.Activity(name = f"Сервер выключен"), status=discord.Status.do_not_disturb)
            time.sleep(1)
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