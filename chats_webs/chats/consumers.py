import json
from django.shortcuts import get_object_or_404
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from .models import Message

# @database_sync_to_async
# def update_user_status(user,status):


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()


    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = str(self.scope['user'])
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'author':author
            }
        )
    
    def chat_message(self,event):
        message = event['message']
        author = get_object_or_404(User,username=event['author'])
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'author': author.username
        }))