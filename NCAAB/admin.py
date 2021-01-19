from django.contrib import admin
from .models import Team, Player, PlayerBoxscore, GameBoxscore


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("abbreviation", "name", "conference")
    search_fields = ("abbreviation", "name", "conference")

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "player_id")
    search_fields = ("name", "player_id")

@admin.register(PlayerBoxscore)
class PlayerBoxscoreAdmin(admin.ModelAdmin):
    list_display = ("player",)
    search_fields = ("player",)

@admin.register(GameBoxscore)
class GameBoxscoreAdmin(admin.ModelAdmin):
    list_display = ("winning_name", "losing_name", "date")
    search_fields = ("winning_name", "losing_name", "date")
