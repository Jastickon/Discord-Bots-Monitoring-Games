import threading
import discord
from discord.ext import commands
from discord.ext import tasks
from mcstatus import JavaServer
import time
import asyncio

TOKEN = "TOKEN" # Ввидите токен вашего бота
IP = "IP"       # Ввидите IP Вашего сервера

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

players=None
async def online1():
    global players
    while True:
        try:
            server = JavaServer.lookup(IP)
            status = server.status()
            time.sleep(20)
            print(f"Данные обновлены до значения {status.players.online}/{status.players.max}")
            players=status.players
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f"онлайн {players.online}/{players.max}"))
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
