#discord_logging

discord_logging is a logging extension module.  
By using this module, logs can be sent by webhook.  

# installing  
Install and update using pip:

`pip install discord_logging`  

A simple example.  
```python
import asyncio
import logging
import discord_logging

WEBHOOK_URL = "Your webhook url"
logger = logging.getLogger()
handler = discord_logging.Discrd_Handler(WEBHOOK_URL)
logger.addHandler(handler)

loop = asyncio.get_event_loop()

async def main():
    logging.info('info')
    logging.debug('debug')
    logging.error('error')
    logging.warning('warning')
    logging.critical('critical')
    print("hello world!")

if __name__ == "__main__":
    loop.create_task(main())
    loop.run_forever()
```
