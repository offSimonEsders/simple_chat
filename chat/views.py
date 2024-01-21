from django.shortcuts import render

from chat.models import Message, Chat


# Create your views here.

def index(request):
    if request.method == 'POST':
        print(f'Recived data {request.POST["message"]}')
        Message.objects.create(text=request.POST["message"], chat=Chat.objects.get(id=2), author=request.user, receiver=request.user)
    chatmessages = Message.objects.filter(chat__id=2)
    return render(request, 'index.html', {'messages': chatmessages})

def auth_view(request):
    return render(request, 'auth.html')