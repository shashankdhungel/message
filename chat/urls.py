from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets

router = DefaultRouter()
router.register( 'chatrooms', ChatRoomViewSets, basename='chatroom')
urlpatterns = router.urls