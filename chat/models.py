from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    members = models.ManyToManyField(User, related_name="chat_room_members")

    def __str__(self):
        return self.name


class Message(models.Model):
    text = models.TextField()
    chatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text + "-" + self.user.username
