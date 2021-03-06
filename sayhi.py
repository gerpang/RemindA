from decouple import config
from telegram.client import Telegram
from datetime import datetime

"""Checks whether the bot is still alive
"""

if __name__ == "__main__":

    tg = Telegram(
    api_id= config('TELEGRAM_API_ID'),
    api_hash= config('TELEGRAM_API_HASH'),
    phone = config('PHONE'),
    database_encryption_key= config('DATABASE_ENCRYPTION_KEY')
    )
    tg.login()
    result = tg.get_chats()
    result.wait()

    if result.error:
        print(f"get chats error: {result.error_info}")
    else:
        print(f"chats: {result.update}")
    
    text="[🤖] It's {}.".format(datetime.now().strftime("%H:%M"))

    result = tg.send_message(
        chat_id=int(config('USER_ID_ME')),  
        text=text,
    )

    result.wait()
    if result.error:
        print(f"send message error: {result.error_info}")
    else:
        print(f"message has been sent: {result.update}")

    tg.stop()
