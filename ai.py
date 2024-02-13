import asyncio
from characterai import PyAsyncCAI

async def main():
    client = PyAsyncCAI('7146a357490379519f16112be070abd695b42bc9')

    char = 'TPpTfGwIkbjhtZE3h3fyMm4MwFyvgwXMJeKSrcl3feg'

    # Getting chat info
    chat = await client.chat2.get_chat(char)

    author = {
        'author_id': chat['chats'][0]['creator_id']
    }

    while True:
        message = input('You: ')

        async with client.connect() as chat2:
            data = await chat2.send_message(
                char, chat['chats'][0]['chat_id'], 
                message, author
            )

        name = data['turn']['author']['name']
        text = data['turn']['candidates'][0]['raw_content']

        print(f"{name}: {text}")

asyncio.run(main())