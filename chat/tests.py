# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Chatroom
from .serializers import ChatRoomSerializer

class ChatRoomViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.chatroom_data = {'name': 'Test Room'}
        self.chatroom = Chatroom.objects.create(name='Existing Room')

    def test_create_chatroom(self):
        response = self.client.post(reverse('chatroom-list'), self.chatroom_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chatroom.objects.count(), 2)  # 1 from setUp and 1 from this test
        self.assertEqual(Chatroom.objects.get(id=response.data['id']).name, 'Test Room')

    def test_get_chatroom(self):
        response = self.client.get(reverse('chatroom-detail', kwargs={'pk': self.chatroom.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.chatroom.name)

    def test_update_chatroom(self):
        updated_data = {'name': 'Updated Room'}
        response = self.client.put(reverse('chatroom-detail', kwargs={'pk': self.chatroom.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.chatroom.refresh_from_db()
        self.assertEqual(self.chatroom.name, 'Updated Room')

    def test_delete_chatroom(self):
        response = self.client.delete(reverse('chatroom-detail', kwargs={'pk': self.chatroom.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Chatroom.objects.count(), 0)

