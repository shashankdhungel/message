from rest_framework import viewsets

from chat.models import Chatroom
from chat.serializers import ChatRoomSerializer


class ChatRoomViewSets(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = Chatroom.objects.all()