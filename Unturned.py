import requests
from bs4 import BeautifulSoup
import threading
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import asyncio

TOKEN = "" # Ввидите токен вашего бота
url = "https://unturned-servers.net/server/12345/" # Ввидите ссылку на ваш сервер с сайта unturned-servers.net
#Пример url = "https://unturned-servers.net/server/288368/"

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

players=None
async def online1():
    global players
    while True:
        try:
            time.sleep(20)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            player_count = soup.find('div', class_='col-12 col-md-7').find_all("tr")[4].find_all("strong")[1].text.replace('	', '').replace('\n','') 
            print(f"Данные обновлены до значения {player_count}")
            players=player_count
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"онлайн {player_count}"))
        except:
            await bot.change_presence(activity=discord.Activity(name = f"Сервер выключен"), status=discord.Status.do_not_disturb)
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
