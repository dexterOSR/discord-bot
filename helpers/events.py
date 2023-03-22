import asyncio
import os
import discord
from discord.ext import commands
from helpers import config_manager


bot_config = config_manager.ConfigManager()



class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} is now online!')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user or message.author.bot:
            return



    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        category_id=bot_config.get_temp_voice_category_id()
        time_before_delte_vc = bot_config.get_time_before_delete_voice_channel()
        
        if before.channel is not None and after.channel is not None:
            if before.channel.id == after.channel.id:
                return
            
        if before.channel is not None and after.channel is None:
            if len(before.channel.members) == 0 and before.channel.category_id == category_id:
                await asyncio.sleep(time_before_delte_vc)
                if len(before.channel.members) == 0:
                    await before.channel.delete()

        if after.channel is not None and before.channel is None:
            if len(after.channel.members) == 0 and after.channel.category_id == category_id:
                await asyncio.sleep(time_before_delte_vc)
                if len(after.channel.members) == 0:
                    await after.channel.delete()

        if after.channel is not None and before.channel is not None:
            if len(before.channel.members) == 0 and before.channel.category_id == category_id:
                await asyncio.sleep(time_before_delte_vc)
                if len(before.channel.members) == 0:
                    await before.channel.delete()

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        category_id_text=bot_config.get_temp_text_category_id()
        category_id_voice=bot_config.get_temp_voice_category_id()
        time_before_delte_tc = bot_config.get_time_before_delete_text_channel()
        time_before_delte_vc = bot_config.get_time_before_delete_voice_channel()

        if channel.category_id == category_id_text or channel.category_id == category_id_voice:
                if channel is None:
                    return
                if isinstance(channel, discord.VoiceChannel):
                    await asyncio.sleep(time_before_delte_vc)
                    if len(channel.members) == 0:
                        await channel.delete()
                    else:
                        return
                elif isinstance(channel, discord.TextChannel):
                    await asyncio.sleep(time_before_delte_tc)
                    await channel.delete()







async def setup(bot):
    await bot.add_cog(Events(bot))