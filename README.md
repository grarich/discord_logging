# discord_logging

discord_logging is a logging extension module.  
By using this module, logs can be sent by webhook.  

# installing  
Install and update using pip:

`pip install discord_logging`  

A simple example.  
```python

import discord

import logging
import discord_logging

logger = logging.getLogger()

WEBHOOK_URL = "Your webhook url"
handler = discord_logging.Discord_Handler(WEBHOOK_URL)

logger.addHandler(handler)

client = discord.Client()


@client.event
async def on_ready():
    print('login！(\'◇\')ゞ')


@client.event
async def on_message(message):
    
    if message.author.bot:
        return
    if message.content == '/hello':
        await message.channel.send('hello')

client.run('THi5IsDuMMyaCCesSTOK3nQ4.Cl2FMQ.ThIsi5DUMMyAcc3s5ToKen7kKWs')
```
