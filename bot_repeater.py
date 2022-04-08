from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession

from config import API_ID, API_HASH, SESSION_STRING, SOURCE_CHANNEL, TARGET_CHANNEL

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)


@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler_new_message(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print('I sended message')

    except Exception as e:
        print(e)

if __name__ == '__main__':
    print("I work!")
    client.start()
    client.run_until_disconnected()
