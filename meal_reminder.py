import argparse
from decouple import config
from telegram.client import Telegram



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("meal", help="Message text")
    args = parser.parse_args()

    tg = Telegram(
    api_id= config('TELEGRAM_API_ID'),
    api_hash= config('TELEGRAM_API_HASH'),
    phone = config('PHONE'),
    database_encryption_key= config('DATABASE_ENCRYPTION_KEY')
    )
    # you must call login method before others
    tg.login()

    # if this is the first run, library needs to preload all chats
    # otherwise the message will not be sent
    result = tg.get_chats()

    # `tdlib` is asynchronous, so `python-telegram` always returns you an `AsyncResult` object.
    # You can wait for a result with the blocking `wait` method.
    result.wait()

    if result.error:
        print(f"get chats error: {result.error_info}")
    else:
        print(f"chats: {result.update}")

    text = """
    [🤖] THIS IS A REMINDER. PLEASE EAT YOUR {}. 
    """.format(args.meal.upper())

    result = tg.send_message(
        chat_id=int(config('USER_ID_BF')),  # args.chat_id,
        text=text,
    )

    result.wait()
    if result.error:
        print(f"send message error: {result.error_info}")
    else:
        print(f"message has been sent: {result.update}")

    tg.stop()
