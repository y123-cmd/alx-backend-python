from django.shortcuts import render
from .models import Message
from django.views.decorators.cache import cache_page

@cache_page(60)  # Cache this view for 60 seconds
def conversation_messages(request, conversation_id):
    messages = Message.objects.filter(conversation_id=conversation_id)
    return render(request, 'chats/conversation.html', {'messages': messages})

