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
# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NjQ3NjA1MTIxOTI4MTM0Njgx.Xdof1Q.K8z6kVw5vIKiyp5WjKPkh-Ll8JY'

# 接続に必要なオブジェクトを生成
selfbot = discord.Client()

# 起動時に動作する処理
@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理ねこ
@bot.command()
async def neko(ctx):
    await ctx.send("にゃーん")

# メッセージ受信時に動作する処理ダンボールは美味い
@bot.command()
async def dan(ctx):
    await ctx.send("世の隅で食べるダンボールは美味いか？")



# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)