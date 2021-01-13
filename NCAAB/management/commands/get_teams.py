from django.core.management.base import BaseCommand, CommandError
from sportsipy.ncaab.teams import Teams
from ...models import Team


class Command(BaseCommand):
    help = 'Get teams'

    def handle(self, *args, **options):
        teams = Teams()
        for team in teams:
            model_team = Team(conference=team.conference,
                              abbreviation=team.abbreviation,
                              name=team.name,)
            model_team.save()
