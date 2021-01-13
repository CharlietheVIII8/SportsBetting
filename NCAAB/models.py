from django.db import models


# Create your models here.

class Team(models.Model):
    conference = models.CharField(max_length=256)
    abbreviation = models.CharField(max_length=256)
    name = models.CharField(max_length=256, primary_key=True)
    games_played = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    win_percentage = models.FloatField(null=True)
    rating = models.FloatField(null=True)
    strength_of_schedule = models.FloatField(null=True)
    conference_wins = models.IntegerField()
    conference_losses = models.IntegerField()
    home_wins = models.IntegerField()
    home_losses = models.IntegerField()
    away_wins = models.IntegerField()
    away_losses = models.IntegerField()
