from discord.ext import commands
import os
import traceback
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_voice_state_update(member, before, after): 
    if member.guild.id == 732216126976819252 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = bot.get_channel(732216127450513430)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。'
            if after.channel.id == 732216127450513431:
                await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。'
            if before.channel.id == 732216127450513431:
                await alert_channel.send(msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')



bot.run(token)
