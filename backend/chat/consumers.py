from channels import consumer
from channels.exceptions import StopConsumer
import json
# from manage import loads

class SearchConsumer(consumer.AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        # print(event['text'])        
        # data = json.loads(event['type'])
        # data = loads.chat_gameR(data)
        # text = json.dumps(data)
        await self.send({
            "type": "websocket.send",
            "text": event['text'],
        })
        
        
    async def websocket_disconnect(self, event):
        await self.send({
            "type": "websocket.disconnect"
        })
        raise StopConsumer