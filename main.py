import discord
import random
from discord.ext import commands


intents = discord.Intents.all()


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def sovet(ctx):
    sovet2 = [
        "Увлажняйте почву перед посадкой растений.",
        "Уделяйте внимание сортировке отходов и переработке органического мусора.",
        "Помните о важности использования экологически чистых удобрений.",
        "Поддерживайте регулярное обновление почвы в горшках для растений."
    ]
    await ctx.send(f'Вот совет по садоводству: {random.choice(sovet2)}')

TOKEN = ''


bot.run(TOKEN)
