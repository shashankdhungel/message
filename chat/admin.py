from django.contrib import admin

from chat.models import Chatroom, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(Chatroom)