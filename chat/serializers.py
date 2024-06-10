from rest_framework import serializers
from chat.models import Chatroom

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatroom
        fields = ['id', 'name']
