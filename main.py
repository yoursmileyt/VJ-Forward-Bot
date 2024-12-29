#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from config import Config
import subprocess
from pyrogram import Client as ACE , idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from typing import Union, Optional, AsyncGenerator
from logging.handlers import RotatingFileHandler
from plugins.regix import restart_forwards
import signal

RESATRT = True

# Auth Users
BOT_OWNER_ID = [ int(chat) for chat in Config.BOT_OWNER_ID.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

def restart_bot():
    os.kill(os.getpid(), signal.SIGTERM)
    

plugins = dict(root="plugins")
if __name__ == "__main__" :
    AceBot = ACE(
        "AceBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins
    )
    
    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially.
        This convenience method does the same as repeatedly calling :meth:`~pyrogram.Client.get_messages` in a loop, thus saving
        you from the hassle of setting up boilerplate code. It is useful for getting the whole chat messages with a
        single call.
        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).
                
            limit (``int``):
                Identifier of the last message to be returned.
                
            offset (``int``, *optional*):
                Identifier of the first message to be returned.
                Defaults to 0.
        Returns:
            ``Generator``: A generator yielding :obj:`~pyrogram.types.Message` objects.
        Example:
            .. code-block:: python
                for message in app.iter_messages("pyrogram", 1, 15000):
                    print(message.text)
        """
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1
               
    async def main():
        await AceBot.start()
        bot_info  = await AceBot.get_me()
        #LOGGER.info(f"<--- @{bot_info.username} Started (c) ACE --->")
        if RESATRT:
            await restart_forwards(AceBot)
        await idle()

    asyncio.get_event_loop().run_until_complete(main())
    #LOGGER.info(f"<---Bot Stopped-->")

    # Check Heroku logs for "Error R14 (Memory quota exceeded)"
    heroku_logs = subprocess.run(["heroku", "logs", "--tail"], capture_output=True, text=True)
    if "Error R14 (Memory quota exceeded)" in heroku_logs.stdout:
        subprocess.run(["heroku", "restart"])  # Restart the bot process on Heroku
