from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets, MessageViewSets
from django.urls import path
from chat.views import sumNumbersView

router = DefaultRouter()
router.register('chatrooms', ChatRoomViewSets, basename='chatroom')
router.register('messages', MessageViewSets, basename='message')
urlpatterns = router.urls

urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]
