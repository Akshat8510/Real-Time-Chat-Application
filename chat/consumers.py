import json
from channels.generic.websocket import AsyncWebsocketConsumer
from groq import Groq
from decouple import config

# Initialize Groq
client = Groq(api_key=config('GROQ_API_KEY'))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data.get('username', 'User')

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat_message', 'message': message, 'username': username}
        )

        # AI Response logic
        if message.lower().startswith('/ai'):
            prompt = message[4:]
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": "user", "content": prompt}]
                )
                ai_response = completion.choices[0].message.content
            except Exception as e:
                ai_response = f"Error calling Groq: {str(e)}"

            await self.channel_layer.group_send(
                self.room_group_name,
                {'type': 'chat_message', 'message': ai_response, 'username': 'Llama-AI'}
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))