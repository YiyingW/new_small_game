from django import forms
from .models import History

class GameForm(forms.ModelForm):
    player_name = forms.CharField(max_length=200)
    comment = forms.TextField()

    class Meta:
        model = History
        fields = ['player_name', 'game_name', 'comment', 'played_time']

    