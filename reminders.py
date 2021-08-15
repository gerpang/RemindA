from telegram.client import Telegram
from decouple import config

bf = config('USER_ID_BF')
tg = Telegram(
    api_id= config('TELEGRAM_API_ID'),
    api_hash= config('TELEGRAM_API_HASH'),
    phone = config('PHONE'),
    database_encryption_key= config('DATABASE_ENCRYPTION_KEY')
)
tg.login()


def new_message_handler(update):
    # we want to process only text messages
    message_content = update["message"]["content"].get("text", {})
    message_text = message_content.get("text", "").lower()

    if message_text == "ping":
        chat_id = update["message"]["chat_id"]
        print(f"Ping has been received from {chat_id}")
        tg.send_message(
            chat_id=chat_id,
            text="pong",
        )


def reply_bf(update):
    message_content = update["message"]["content"].get("text", {})
    message_text = message_content.get("text", "").lower()
    chat_id = update["message"]["chat_id"]
    sender = update['message']['sender']['user_id']
    with open('rough/logs.txt','a+') as f:
        f.write("[{}] {}: {}\n".format(chat_id, sender,message_text))
    if chat_id == bf and sender == bf and message_text == "hi":
        tg.send_message(
            chat_id=chat_id,
            text="~~ hi yourself, handsome!~ <3<3",
        )


# tg.add_message_handler(new_message_handler)
tg.add_message_handler(reply_bf)
tg.idle()
