from django import forms
from .models import History

class GameForm(forms.ModelForm):
    player_name = forms.CharField(min_length=1, max_length=200)
    comment = forms.CharField(min_length=1, max_length=2000)

    class Meta:
        model = History
        fields = ['player_name', 'comment']

