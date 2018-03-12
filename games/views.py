from django.shortcuts import HttpResponse, render
from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'games/home.html', {})

def detail(request, game_id):
    if game_id == '0' or game_id == '1':
        return render(request, 'games/game.html', {"game_id": game_id})
    else:
        return render(request, 'games/developing.html', {})
