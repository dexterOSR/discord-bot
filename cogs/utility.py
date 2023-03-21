import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="ping",
        description="Muestra la latencia actual del bot.",
        aliases=['p', 'latency']
    )
    async def ping(self, ctx):
        embed = discord.Embed(
            title="🏓 ¡PONG!",
            description=f"La latencia actual del bot es de {round(self.bot.latency * 1000)} ms.",
            color=0x70a2d4,
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))