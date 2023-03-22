import discord
from discord.ext import commands
from helpers import config_manager
from helpers.utils import category_channels

bot_config = config_manager.ConfigManager()


class Channels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @category_channels(bot_config.get_temp_voice_category_id(),
                       bot_config.get_maximum_temp_voice_channels())
    @commands.hybrid_command(
        name="temp_voice",
        description="Crea un canal de voz temporal.",
        aliases=['tvoice']
    )
    
    async def temp_voice(self, ctx, name=None, user_limit = 2):
        category = ctx.guild.get_channel(bot_config.get_temp_voice_category_id())
        time_before_deleting_vc = bot_config.get_time_before_delete_voice_channel()

        if name is None:
            name = f"{ctx.author.name}"

        if not (2 <= user_limit <= 20):
            await ctx.send("El número de miembros del canal de voz debe ser entre 2 y 20.")
            return

        voice_channel = await category.create_voice_channel(name=name, user_limit=user_limit)

        voice_state = ctx.author.voice

        if voice_state is None:
            await ctx.send(f"{ctx.author.mention} Tú canal de voz '{name}' fue creado correctamente, sin embargo no te hemos podido mover a el de manera automática. Recuerda que el canal de voz se eliminará automáticamente después de que este permanezca vacío por {time_before_deleting_vc} segundos.")
        else:
            await ctx.send(f"{ctx.author.mention} Tú canal de voz '{name}' fue creado correctamente. Recuerda que el canal de voz se eliminará automáticamente después de que este permanezca vacío por {time_before_deleting_vc} segundos.")
            await ctx.author.move_to(voice_channel)


    @category_channels(bot_config.get_temp_text_category_id(),
                       bot_config.get_maximum_temp_text_channels())
    @commands.hybrid_command(
        name="temp_text",
        description="Crea un canal de texto temporal.",
        aliases=['ttext']
    )
    async def temp_text(self, ctx, name=None):
        
        category = ctx.guild.get_channel(bot_config.get_temp_text_category_id())
        time_before_deleting_tc = bot_config.get_time_before_delete_text_channel()

        if name is None:
            name = f"{ctx.author.name}"

        await ctx.guild.create_text_channel(name=name, category=category)
        await ctx.send(f"{ctx.author.mention} Tú canal de texto '{name}' fue creado correctamente. Recuerda que el canal será eliminado automáticamente después de {time_before_deleting_tc} segundos.")




async def setup(bot):
    await bot.add_cog(Channels(bot))