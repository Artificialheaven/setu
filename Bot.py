import asyncio
import websockets
import json
import requests

class Bot:

    url = '127.0.0.1'
    http_port = '5700'
    ws_port = '8888'

    def __init__(self,u,h,w):
        self.url = u
        self.http_port = h
        self.ws_port = w

    def sendGroupMsg(self,group_id,msg):
        #发送群聊消息
        return requests.get(f'http://{self.url}:{self.http_port}/send_group_msg?group_id={group_id}&message={msg}').text
    def sendPrivateMsg(self,user_id,msg):
        #发送私聊消息
        return requests.get(f'http://{self.url}:{self.http_port}/send_private_msg?user_id={user_id}&message={msg}').text

    async def run(self,receiveGroupMsg,receivePrivateMsg):
        async with websockets.connect(f"ws://{self.url}:{self.ws_port}") as websocket:
            #await websocket.send("Hello world!")
            while True:
                a = await websocket.recv()
                #print(a)
                js = json.loads(a)
                # js['post_type'] = ‘message’    js['message_type'] = 'group/private'
                try:
                    post_type = js['post_type']
                    message_type = js['message_type']
                    if message_type == 'group':
                        group_id = js['group_id']
                        user_id = js['sender']['user_id']
                        msg = js['raw_message']
                        print(f'{post_type}|{message_type}[{group_id}]({user_id}){msg}')
                        receiveGroupMsg(group_id, user_id, msg)
                    elif message_type == 'private':
                        user_id = js['sender']['user_id']
                        msg = js['raw_message']
                        print(f'{post_type}|{message_type}({user_id}){msg}')
                        receivePrivateMsg(user_id, msg)
                        #await websocket.send('{"action":"send_private_msg","params":{"user_id":%s,"message":"hello"}}' % user_id)
                except:
                    continue

if __name__ == "__main__":
    asyncio.run(run())