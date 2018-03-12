from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class History(models.Model):
    def __str__(self):
        return self.player_name + " : " + self.game_name

    player_name = models.CharField(max_length=200)
    game_name = models.CharField(max_length=200)
    comment = models.TextField()
    played_time = models.DateTimeField('time played')

