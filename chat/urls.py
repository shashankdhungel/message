from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets, MessageViewSets
from django.urls import path
from chat.views import sumNumbersView
from chat.viewsets import RegisterView,UserViewSet

router = DefaultRouter()
router.register('chatrooms', ChatRoomViewSets, basename='chatroom')
router.register('messages', MessageViewSets, basename='message')
router.register(r'users', UserViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('sum_num/', sumNumbersView, name='sum_numbers'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
