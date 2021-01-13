from django.db import models


# Create your models here.

class Team(models.Model):
    conference = models.CharField(max_length=256)
    abbreviation = models.CharField(max_length=256)
    name = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.name
