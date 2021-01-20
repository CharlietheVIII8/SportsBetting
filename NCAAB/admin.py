from django.contrib import admin
from .models import Team, PlayerBoxscore, GameBoxscore, Tweet, TwitterAccount


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("abbreviation", "name", "conference")
    search_fields = ("abbreviation", "name", "conference")


@admin.register(PlayerBoxscore)
class PlayerBoxscoreAdmin(admin.ModelAdmin):
    list_display = ("player",)
    search_fields = ("player",)


@admin.register(GameBoxscore)
class GameBoxscoreAdmin(admin.ModelAdmin):
    list_display = ("winner", "loser", "date")
    search_fields = ("winner", "loser", "date")


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("account",)
    search_fields = ("account",)


@admin.register(TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "handle")
    search_fields = ("name", "handle")
