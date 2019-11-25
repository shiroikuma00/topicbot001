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

# トピックス
@bot.command()
async def randomtopic(ctx, topic_name =None):
    topic = False
    if not topic_name:
        topic_name = "simple"

if topic_nam == "deep":   
    deep = ["自分を「弱い人間」と感じた瞬間は？", 
            "ありのままの自分でいられる場所は？", 
            "今のあなたに大きな影響を与えた人物は？", 
            "もしあと一日しか生きられないとしたら、最初に何をする？", 
            "小さい頃の夢は？", 
            "一番好きなダンボールは何？", 
            "収入のことを考えなくてもよければ就きたい職業は？", 
            "あなたが最も恐れているものは何？", 
            "人生の中でやらかした最もクレイジーなことは？", 
            "犬派？猫派？", 
            "人生で欠けていると感じるものは？", 
            "ダンボールで実現したい夢は？", 
            "ダンボールの好きなところは？"]
    topic = True

if topic_name == "simple":
    list = ["ゲーム","お菓子","アニメ","YouTube","Discord"]
    topic = True
    
    elif topic_name == "discord":
        list = ["サーバー","世の隅の端","雑コム","ごち雑"]
        topic = True

    verd = ["の好きなところは？","の面白いところは？","で自分が作ってみるなら？"]  :

    choice1 = random.choice(deep)
    choice2 = random.choice(list)
    choice3 = random.choice(verd)
    

 if topic == True:
        topic_c = (f"{choice1}" or f"{choice2}{choice3}")
        edit = await ctx.send(f"今の旬なトピックは...")
        await sleep(5)
        await edit.edit(f"今の旬なトピックはこれ！\n``{topic_c}")

# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)