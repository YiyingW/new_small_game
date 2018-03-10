from django.shortcuts import HttpResponse, render
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'games/home.html', {})

def detail(request, game_id):
    if game_id == '0':
        return render(request, 'games/game_0.html', {})
    elif game_id == '1':
        return render(request, 'games/game_1.html', {})
    else:
        return render(request, 'games/developing.html', {})
