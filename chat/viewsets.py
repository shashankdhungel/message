from rest_framework import viewsets

from chat.models import Chatroom, message
from chat.serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSets(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = Chatroom.objects.all()

class MessageViewSets(viewsets.ModelViewSet):
    serializer_class = MessageSe
    queryset = message.objects.all()
