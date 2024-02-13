import pyvts
from characterai import PyAsyncCAI
import asyncio

async def connect_auth(myvts):
    ''' functions to get authenticated '''
    await myvts.connect()
    await myvts.request_authenticate_token()
    await myvts.request_authenticate()
    await myvts.close()

async def trigger(myvts):
    ''' function to trigger hotkey '''
    await myvts.connect()
    await myvts.request_authenticate()
    response_data = await myvts.request(myvts.vts_request.requestHotKeyList())
    print(response_data)
    hotkey_list = []
    for hotkey in response_data["data"]["availableHotkeys"]:
        hotkey_list.append(hotkey["name"])
    send_hotkey_request = myvts.vts_request.requestTriggerHotKey(hotkey_list[0])
    print(hotkey_list[0])
    await myvts.request(send_hotkey_request)  # send request to play 'My Animation 1'
    print("emoticonated!")
    await myvts.close()

async def main(vts):
    client = PyAsyncCAI('7146a357490379519f16112be070abd695b42bc9')

    char = 'sEiSmGMnzTdaO7PxIcAPhccXGUh6OPt57E-r595wbE0'

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

        await trigger(vts)

        print(f"{name}: {text}")

if __name__ == "__main__":
    ''' using different functions '''
    myvts = pyvts.vts()
    asyncio.run(connect_auth(myvts))
    asyncio.run(main(myvts))

    