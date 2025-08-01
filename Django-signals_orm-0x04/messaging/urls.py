from django.urls import path
from .views import delete_user
from .views import send_message, inbox

urlpatterns = [
    path('delete_user/', delete_user, name='delete_user'),
    path('send/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
]
