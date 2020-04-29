  
import aiohttp
import asyncio
import logging
from logging import Handler
import urllib.parse

class AioHTTPHandler(Handler):

    def __init__(self, url):
        logging.Handler.__init__(self)
        self.url = url

    def mapLogRecord(self, record):
        return record.__dict__

    def emit(self, record):
        asyncio.create_task(self.emitting(record))

    async def emitting(self, record):
        try:
            msg = self.format(record)
            url = self.url
            headers = {}
            data = self.mapLogRecord(record)
            headers["Content-type"] = "application/x-www-form-urlencoded"
            #can't do anything with the result
            async with aiohttp.request("POST", url, data={content:f"{msg}"}, headers=headers):
                pass
        except Exception:
            self.handleError(record)
