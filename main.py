from pyrogram import Client
import asyncio
from .configs import *

from datetime import datetime

bot = Client(
	"mtproto1",
    api_id=api_id,          ## your api_id that you got from https://my.telegram.org/apps
    api_hash=api_hash,      ## your api_hash that you got from https://my.telegram.org/apps

)


now = datetime.now()
current_time = now.strftime("%H:%M")








async def send(current_time):
    while True:
        now1 = datetime.now()
        current_time1 = now1.strftime("%H:%M")
        if current_time1 != current_time:

            async with bot :
                await bot.update_profile(bio=f"تو مرا جانو جهانی ...{current_time1}") ## your dsire bio and the current time
            current_time=current_time1






bot.run(send(current_time))

