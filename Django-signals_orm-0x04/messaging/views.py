from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')  

        receiver = get_object_or_404(User, id=receiver_id)
        parent_message = None

        if parent_id:
            parent_message = Message.objects.get(id=parent_id)

        Message.objects.create(
            sender=request.user,          
            receiver=receiver,            
            content=content,
            parent_message=parent_message
        )
        return redirect('inbox')  

    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messaging/send_message.html', {'users': users})

