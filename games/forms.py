from django import forms
from .models import History

class GameForm(forms.ModelForm):
    player_name = forms.CharField(min_length=1, max_length=200)
    comment = forms.CharField(
                            widget=forms.Textarea(
                                attrs={'rows':5, 'placeholder': 'What is on your mind?'}
                            ),
                            min_length=1, 
                            max_length=4000)  # TODO: this placeholder is not working.

    class Meta:
        model = History
        fields = ['player_name', 'comment']

