from rest_framework import viewsets
from django.contrib.auth.models import User
from chat.models import Chatroom, Message
from chat.serializers import ChatRoomSerializer, MessageSerializer, RegisterSerializer, UserSerializer
from rest_framework import generics


class ChatRoomViewSets(viewsets.ModelViewSet):
    serializer_class = ChatRoomSerializer
    queryset = Chatroom.objects.all()

class MessageViewSets(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer