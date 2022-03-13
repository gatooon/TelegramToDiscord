from ReadFiles import ReadFiles
from telethon import TelegramClient, events
import shutil

read_file = ReadFiles()
conf_dic = read_file.getTelegramConf()
TELEGRAM_API_ID = conf_dic["telegram_api_id"]
TELEGRAM_API_HASH = conf_dic["telegram_api_hash"]
TELEGRAM_HOOK_CHANNEL_NAME = ""

MESSAGE_FILE_PATH = "assets/downloads/message.txt"

telegram_client = TelegramClient("aon", TELEGRAM_API_ID, TELEGRAM_API_HASH)

@telegram_client.on(events.NewMessage(chats=TELEGRAM_HOOK_CHANNEL_NAME))
async def listenNewMessage(message):
    if message.text:
        f = open(MESSAGE_FILE_PATH, "w")
        f.write(message.text)
        f.close()
        shutil.move(MESSAGE_FILE_PATH, "assets/")

telegram_client.start()
telegram_client.run_until_disconnected()