from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets, MessageViewSets

router = DefaultRouter()
router.register( 'chatrooms', ChatRoomViewSets, basename='chatroom')
router.register( 'messages', MessageViewSets, basename='message')
urlpatterns = router.urls