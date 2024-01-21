from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from chat.models import Message, Chat


# Create your views here.

def index(request):
    if request.method == 'POST':
        print(f'Recived data {request.POST["message"]}')
        Message.objects.create(text=request.POST["message"], chat=Chat.objects.get(id=2), author=request.user,
                               receiver=request.user)
    chatmessages = Message.objects.filter(chat__id=2)
    return render(request, 'index.html', {'messages': chatmessages})


def auth_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if (user):
            login(request, user)
            return HttpResponseRedirect('/chat/')
    return render(request, 'auth.html')


def register_view(request):
    response = { 'message': 'ok' }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if (username and password):
            try:
                User.objects.create_user(username=username, password=password)
                return HttpResponseRedirect('/login/')
            except:
                response.update({'message': 'error'})
        else:
            response.update({'message': 'error'})
    return render(request, 'register.html', response)
