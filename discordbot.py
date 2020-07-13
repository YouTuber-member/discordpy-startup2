
#インストールしたdiscord.pyの読み込み
import discord 
import os
#randomモジュールの読み込み
import random
#reライブラリの読み込み
import re

import time 



#翠のトークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#接続に必要なオブジェクトを生成
client = discord.Client()






from time import 
time_then = time.monotonic() 
pinger = await client.send_message(message.channel, '__*`Pinging...`*__') 
ping = '%.2f' % (1000*(time.monotonic()-time_then)) 
await client.edit_message(pinger, ':ping_pong: \n **Pong!** __**`' + ping + 'ms`**__') # you can edit this to say whatever you want really. Hope this helps. 
















#起動時に動作する処理
@client.event
async def on_ready():
    print('Hello World,対話botプログラム「Project-noa-」、起動しました')

#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return 
#会話
 #おはよう
    #「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
    G_lis = ['今日も一日頑張りましょうね！','いってらっしゃいませー！']
    respon = random.choice(G_lis)
    if message.content.startswith('おはよ') or message.content == 'ぐっもーにん':
        await message.channel.send('おはようございます、' + message.author.name + 'さん！( ⑉¯ ꇴ ¯⑉ )\n' + respon)
 #おやすみ
    #「おやすみ」と発言したら「おやすみなさい！」と返す処理
    if message.content.startswith('おやすみ'):
        await message.channel.send('おやすみなさい、良い夢を見てくださいね！(｡•̀ᴗ-)✧')
 #おやすみ
    #「おやすみ」と発言したら「おやすみなさい！」と返す処理
    if message.content.startswith('!e help'):
        await message.channel.send('どもどもヘルプを表示するね\n > 1.YouTubeと打つとエンジェルコア君のYouTubeチャンネルが表示されます')
        
        #おわ
    #「おわ」でメッセージが終わった場合労う
    if '@@エンジェルBOT!#2005 ' in message.content:
        await message.channel.send('ハイなんでしょう!e help でヘルプが見れます')	
        
         #おわ
    #「おわ」でメッセージが終わった場合労う
    if '@695145741391495209' in message.content:
        await message.channel.send('ハイなんでしょう!e help でヘルプが見れます')	
 #おわ
    #「おわ」でメッセージが終わった場合労う
    if 'おわ' in message.content:
        await message.channel.send('お疲れ様です！∠(｀･ω･´)')	
        #おわ
    #「おわ」でメッセージが終わった場合労う
    if 'こん' in message.content:
        await message.channel.send('こんにちは' + message.author.name + 'さん')	
        #おわ
    #「おわ」でメッセージが終わった場合労う
    if 'お疲れ' in message.content:
        await message.channel.send('お疲れ様です！∠(｀･ω･´)')	
            #「おわ」でメッセージが終わった場合労う
    if 'おつかれ' in message.content:
        await message.channel.send('お疲れぇ')
                    #「おわ」でメッセージが終わった場合労う
    if 'you' in message.content:
        await message.channel.send('https://www.youtube.com/channel/UC3B74ty4c5XXDGqjB_LYHQA')
                    #「おわ」でメッセージが終わった場合労う
    if 'You' in message.content:
        await message.channel.send('https://www.youtube.com/channel/UC3B74ty4c5XXDGqjB_LYHQA')
 #褒め
    #「可愛い」と言うと照れる
    if message.content == '可愛い！' or message.content == 'かわいい！':
        await message.channel.send('( ﻿˶﻿ˆ꒳ˆ˵﻿ )ｴﾍﾍ、褒めても何も出ませんよ！')
 #御籤 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    if message.content == 'おみくじ' or message.content == '今日の運勢は？':
        prob = random.random()
    
        if prob < 0.3:
            await message.channel.send('凶です……外出を控えることをオススメします(  ･᷄ὢ･᷅  )')
        
        elif prob < 0.65:
            await message.channel.send('吉です！何かいい事があるかもですね！')
        
        elif prob < 0.71:
            await message.channel.send('末吉……どれくらい運がいいんでしょうね？•́ω•̀)?')
        
        elif prob < 0.76:
            await message.channel.send('半吉は吉の半分、つまり運がいいのです！')
        
        elif prob < 0.80:
            await message.channel.send('小吉ですね！ちょっと優しくされるかも？')
        
        elif prob < 0.83:
            await message.channel.send('吉の中で1番当たっても微妙に感じられる……つまり末吉なのです( ´･ω･`)')
       
        elif prob <= 1.0:
            await message.channel.send('おめでとうございます！大吉ですよ！(๑>∀<๑)♥')
            
            
            #御籤 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    if message.content == 'さいころ' or message.content == 'サイコロ':
        prob = random.random()
    
        if prob < 0.83:
            await message.channel.send('1')
        
        elif prob < 0.83:
            await message.channel.send('2')
        
        elif prob < 0.83:
            await message.channel.send('3')
        
        elif prob < 0.83:
            await message.channel.send('4')
        
        elif prob < 0.83:
            await message.channel.send('5')
        
        elif prob < 0.83:
            await message.channel.send('6')
       

 #埋込みメッセージ「議題」
    if '議題作成' in message.content:
        match = re.search(r".*タイトルは(.+)、サブタイトルは(.+)。.*", message.content)
        if match:
            title, subtitle = match.groups()
            embed = discord.Embed(title=title, description=subtitle,color=discord.Color.green())
            await message.channel.send(embed=embed)

#自動会話
 #笑
    lis = ['笑うのは体にいいことなのです！','ꉂꉂ(>ᗜ<*)']
    res = random.choice(lis)
    
    if (message.content.endswith(('笑','w')) and random.random() > 0.75):
        await message.channel.send(res)
 #ほえー
    li = ['ほえー','わー','えへっ']
    resp = random.choice(li)
    
    if message.content == 'おはよ':
        pass
    elif (message.content.endswith(('よ','かぁ')) and random.random() < 0.4):
        await message.channel.send(resp)
        

#ウェルカムメッセージ
@client.event
async def on_member_join(member):
   await client.get_channel(578909248902266883).send(f'ようこそ、**{member.mention}**さん！あなたの訪問を歓迎させていただきます、対話botのノアと申します！ まだ不完全な状態ですがよろしくお願いします！')

#リムーブメッセージ
@client.event
async def on_member_remove(member):
    await    client.get_channel(578909248902266883).send(f'**{member.name}が退室しました。またの訪問をお待ちしております！**')

#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
