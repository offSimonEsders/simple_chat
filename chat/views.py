from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        print('Recived data')
    return render(request, 'index.html', {'username': request.user})