from django.contrib import admin
from .models import Team


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
