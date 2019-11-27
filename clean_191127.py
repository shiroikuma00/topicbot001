# インストールした discord.py を読み込む
# coding: UTF-8
from asyncio import sleep
import discord
import datetime
import typing
import random
import asyncio
from discord.ext import tasks
import numpy as np
import aiofiles
import time
import re
import feedparser
import json
import traceback
import math
import pathlib
import platform
import math
import sqlite3
import zipfile
import os
import requests
import json
import random
from discord.ext import commands


bot = commands.Bot(command_prefix=['99'])
selfbot = discord.Client()
bot.remove_command('help')
# 自分のBotのアクセストークン
TOKEN = 'NjQ3NjA1MTIxOTI4MTM0Njgx.XduvEg.JHlRalxuf-2IqqoNuitBFOo5l90'

# 接続に必要なオブジェクトを生成
selfbot = discord.Client()

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@bot.command()
async def gomi(ctx):
    await ctx.send("お掃除♪お掃除♪")

# 書き込み削除
@commands.has_permissions(manage_messages=True,delete =None)
@bot.command()
    if not delete:
        delete = "delete"
# 書き込み削除(件数未設定)
    if delete == "delete":
    async def delete(ctx,limit):
        limit = int(300)
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'{ctx.author.mention}->お掃除完了しました！')
        Instructions = True
# 書き込み削除(件数設定済)
    elif delete == "delete {}":
        limit = int(300)
        Instructions = True
    else:
        await ctx.send(f"どういう指示ですか？``{delete}``なんて知らないです！")
# 書き込み削除(繰り返しあり)
@tasks.loop(minutes)
async def delete_loop():
    ch = bot.get_channel(# 書き込んだチャンネルID取得)
    await ch.purge()

delete_loop.start()

# ヘルプ
@bot.command()
async def help(ctx, cmd =None):
    helpc = await ctx.send(f"{ctx.author.mention}->ちょっと待ってね。ヘルプ情報を探しています...")
    if cmd == None:
        embed=discord.Embed(title="ゴミ回収業者ごみちゃん ヘルプ", description="ゴミ回収業者のコマンドリストです。", color=0xffd700)
        embed.add_field(name="Prefix = [ 99 ]", value="``purge``, ``delete_loop``, ``gomi``, ``hogehoge``", inline=False)
        embed.set_footer(text="【99help <コマンド>】と入力すると、コマンドの詳細情報を確認できます。")
        await helpc.edit(content=f"{ctx.author.mention}->",embed=embed)
    elif cmd == "delete":
        embed=discord.Embed(title="ゴミ回収業者ごみちゃん ヘルプ", color=0xffd700)
        embed.add_field(name="``delete``", value="書き込みを300件削除する設定ができます。", inline=False)
        embed.add_field(name="Values",value="``l1create <your IGN>``", inline=False)
        embed.set_footer(text=f"Command used by {ctx.author.name}")
        await helpc.edit(content=f"{ctx.author.mention}->",embed=embed)
    elif cmd == "delete_loop":
        embed=discord.Embed(title="ゴミ回収業者ごみちゃん ヘルプ", color=0xffd700)
        embed.add_field(name="``delete_loop``", value="定期的に削除する設定ができます。", inline=False)
        embed.add_field(name="Values",value="``l1create <your IGN>``", inline=False)
        embed.set_footer(text=f"Command used by {ctx.author.name}")
        await helpc.edit(content=f"{ctx.author.mention}->",embed=embed)
    elif cmd == "gomi":
        embed=discord.Embed(title="ゴミ回収業者ごみちゃん ヘルプ", color=0xffd700)
        embed.add_field(name="``gomi``", value="定期的に削除する設定ができます。(仮)", inline=False)
        embed.add_field(name="Values",value="``l1create <your IGN>``", inline=False)
        embed.set_footer(text=f"Command used by {ctx.author.name}")
        await helpc.edit(content=f"{ctx.author.mention}->",embed=embed)
    elif cmd == "hogehoge":
        embed=discord.Embed(title="ゴミ回収業者ごみちゃん ヘルプ", color=0xffd700)
        embed.add_field(name="``hogehoge``", value="定期的に削除する設定ができます。(仮)", inline=False)
        embed.add_field(name="Values",value="``l1create <your IGN>``", inline=False)
        embed.set_footer(text=f"Command used by {ctx.author.name}")
        await helpc.edit(content=f"{ctx.author.mention}->",embed=embed)
        
# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)