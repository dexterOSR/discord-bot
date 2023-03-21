import asyncio
import discord
from discord.ext.commands import Bot
from helpers import config_manager
import os

bot_config = config_manager.ConfigManager()

bot = Bot(
    command_prefix='!',
    help_command=None,
    intents=discord.Intents.all()
)


async def load_cogs():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

    await bot.load_extension('helpers.events')



asyncio.run(load_cogs())


if __name__ == '__main__':
    bot.run(bot_config.get_discord_token())