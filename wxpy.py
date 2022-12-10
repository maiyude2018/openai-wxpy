# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *
import time

# 调用机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    apikey="Bearer sk-dvGk9z3"
    headers = {'Authorization': apikey,}
    json_data = {
        'model': 'text-davinci-003',
        'prompt': text,
        'temperature': 0.1,
        'max_tokens': 512,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    r = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
    rjson=r.json()
    retext = "chatGPT:" + rjson["choices"][0]["text"]
    print(retext)
    return retext




bot = Bot(cache_path=True)
#bot = Bot()

@bot.register()
def forward_message(msg):
    bot_name = "@" + (str(msg.bot).replace("<Bot: ","").replace(">",""))
    #print(msg)
    if bot_name in str(msg.text) or "@Fisher" in str(msg.text):
        print("收到",msg.text)
        if msg.type == "Text":
            msgs = str(msg.text).replace(bot_name,"")
            return auto_reply(msgs)


embed()

