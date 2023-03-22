import asyncio
from discord.ext import commands


def category_channels(category_id, number=1):
    async def predicate(ctx):
        category = ctx.guild.get_channel(category_id)
        if not category:
            await ctx.send("No se ha encontrado la categoria.")
            return False
        channels = category.channels
        if len(channels)+1 > number:
            await ctx.send(f"Demasiados canales temporales creados. El máximo permitido es {number} canales.")
            return False
        return True
    return commands.check(predicate)

