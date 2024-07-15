from rest_framework import serializers
from chat.models import Chatroom, Message

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['id', 'name', 'created_by']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'chatroom', 'user']
        