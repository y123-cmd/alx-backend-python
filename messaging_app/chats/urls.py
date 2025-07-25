from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet
from rest_framework_nested.routers import NestedDefaultRouter 
from rest_framework.routers import DefaultRouter
from .auth import (
    RegisterUserAPIView,
    LoginUserAPIView,
    LogoutUserAPIView
)


router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')

nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
    path('auth/register/', RegisterUserAPIView.as_view(), name='register'),
    path('auth/login/', LoginUserAPIView.as_view(), name='login'),
    path('auth/logout/', LogoutUserAPIView.as_view(), name='logout'),
]