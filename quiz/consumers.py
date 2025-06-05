import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ResultConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("results", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("results", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "results",
            {
                "type": "broadcast_result",
                "message": data["message"]
            }
        )

    async def broadcast_result(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
