from django.shortcuts import HttpResponse, render, redirect
from django.views import generic
from django.urls import reverse
from .forms import GameForm
from .models import History
from datetime import datetime
import requests

# Create your views here.
def index(request):
    return render(request, 'games/home.html', {})

def detail(request, game_id):
    game_map = {'0': "Connect4Game", '1': "Number Game"}
    if request.method == "GET":
        if game_id == '0' or game_id == '1':
            return render(request, 'games/game.html', {"game_id": game_id})
        elif game_id == '2':
            response = requests.get('http://freegeoip.net/json/')
            geodata = response.json()
            return render(request, 'games/map.html', {
                'time zone': geodata['time_zone'],
                'country': geodata['country_name'],
                'latitude': geodata['latitude'],
                'longitude': geodata['longitude'],
                'api_key': "AIzaSyDJDxy3ex0Y0FByMHmmMEOp5lI0FWmUZvY"
            })
        else:
            return render(request, 'games/developing.html', {})
    elif request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            player_name = record.player_name
            game_name = game_map[game_id]
            comment = record.comment
            played_time = datetime.now()
            history = History.objects.create(
                player_name = player_name,
                game_name = game_name,
                comment = comment,
                played_time = played_time
            )
            return redirect(reverse('summary'))
        else:
            form = GameForm()
        return render(request, 'games/game.html', {"game_id": game_id})

def summary(request):
    records = History.objects.all()
    return render(request, 'games/summary.html', {"records": records})






