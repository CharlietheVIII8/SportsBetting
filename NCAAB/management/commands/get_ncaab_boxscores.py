from django.core.management.base import BaseCommand, CommandError
from sportsipy.ncaab.boxscore import Boxscore, Boxscores
from sportsipy.ncaab.player import AbstractPlayer
from ...models import Team, GameBoxscore, PlayerBoxscore
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Get boxscores'

    def handle(self, *args, **options):
        boxscores = Boxscores(date=datetime.now() - timedelta(days=2), end_date=datetime.now())
        for date, data in boxscores.games.items():
            print(date)
            for game in data:
                print(game)
                boxscore = Boxscore(game['boxscore'])
                game_dict = boxscore.dataframe.to_dict('records')[0]
                del game_dict['winning_name']
                del game_dict['losing_name']
                del game_dict['winner']
                del game_dict['date']
                date = datetime.strptime(boxscore.date, '%B %d, %Y')
                game, created = GameBoxscore.objects.update_or_create(date=date,
                                                                      winner=Team.objects.get(
                                                                          abbreviation=boxscore.winning_abbr),
                                                                      loser=Team.objects.get(
                                                                          abbreviation=boxscore.losing_abbr),
                                                                      defaults=game_dict)
                home_team = boxscore.home_players
                away_team = boxscore.away_players
                for player in home_team + away_team:
                    player_dict = player.dataframe.to_dict('records')[0]
                    player_dict['game'] = game
                    PlayerBoxscore.objects.update_or_create(player=player.name, date=date, defaults=player_dict)
