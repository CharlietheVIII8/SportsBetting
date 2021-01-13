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
                              name=team.abbreviation,
                              games_played=team.games_played,
                              wins=team.wins,
                              losses=team.losses,
                              win_percentage=team.win_percentage,
                              rating=team.,
                              strength_of_schedule=team.strength_of_schedule,
                              conference_wins=team.conference_wins,
                              conference_losses=team.conference_losses,
                              home_losses=team.home_losses,
                              home_wins=team.home_wins,
                              away_losses=team.away_losses,
                              away_wins=team.away_wins)
            model_team.save()
