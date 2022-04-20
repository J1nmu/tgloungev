from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import GetFullChannelRequest
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Telegram

APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
FROM_ = config("FROM_CHANNEL")
TO_ = config("TO_CHANNEL")

FROM = [str(i) if 'https' in i else int(i) for i in FROM_.split()]
TO = [str(i) for i in TO_.split()]

try:

    BotzHubUser = TelegramClient('testBot2', APP_ID, API_HASH)
    BotzHubUser.start()
    print("Connected succesfully")

except Exception as ap:

    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(chats=FROM))

async def sender_bH(event):

    if event.chat.id == 1569758255:

        group_link = "From: " + "Kingdom of X100 CALLS Chat"
    
    elif event.chat.id == 1789551115:

        group_link = "From: " + "The iLLest Discussions"

    for i in TO:
   
        try:

            if event.chat.id == 1569758255 or event.chat.id == 1789551115:

                if "T.ME" in event.message.message.upper():

                    await BotzHubUser.send_message(
                        i,
                        group_link + "--------\n" + event.message.message
                    )

                    print("-- Sending TG")

        except Exception as e:

            print(e)

print("Bot has started.")

BotzHubUser.run_until_disconnected()