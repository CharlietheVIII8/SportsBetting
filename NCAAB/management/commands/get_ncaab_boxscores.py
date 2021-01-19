from django.core.management.base import BaseCommand, CommandError
from sportsipy.ncaab.boxscore import Boxscore
from sportsipy.ncaab.player import AbstractPlayer
from ...models import Team, GameBoxscore, PlayerBoxscore, Player
from datetime import datetime


class Command(BaseCommand):
    help = 'Get boxscores'

    def handle(self, *args, **options):
        boxscore = Boxscore('2017-11-10-21-kansas')
        game_dict = boxscore.dataframe.to_dict('records')[0]
        date = datetime.strptime(boxscore.date, '%B %d, %Y')
        game, created = GameBoxscore.objects.update_or_create(date=date,
                                                              winning_name=Team.objects.get(name=boxscore.winning_name),
                                                              losing_name=Team.objects.get(name=boxscore.losing_name),
                                                              defaults=game_dict)
        home_team = boxscore.home_players
        away_team = boxscore.away_players
        for player in home_team + away_team:
            abstract_player = AbstractPlayer(player._player_id)
            model_player, created = Player.objects.update_or_create(player_id=abstract_player.player_id,
                                                                    name=abstract_player.name,
                                                                    defaults={
                                                                        'minuted_played': abstract_player.minutes_played,
                                                                        'field_goals_made': abstract_player.field_goals,
                                                                        'field_goals_attempted': abstract_player.field_goal_attempts,
                                                                        'field_goal_percentage': abstract_player.field_goal_percentage,
                                                                        'three_pointers_made': abstract_player.three_pointers,
                                                                        'three_pointers_attempted': abstract_player.three_point_attempts,
                                                                        'three_point_percentage': abstract_player.three_point_percentage,
                                                                        'two_pointers_made': abstract_player.two_pointers,
                                                                        'two_point_percentage': abstract_player.two_point_percentage,
                                                                        'two_pointers_attempted': abstract_player.two_point_attempts,
                                                                        'effective_field_goal_percentage': abstract_player.effective_field_goal_percentage,
                                                                        'free_throws_made': abstract_player.free_throws,
                                                                        'free_throw_percentage': abstract_player.free_throw_percentage,
                                                                        'free_throws_attempted': abstract_player.free_throw_attempts,
                                                                        'total_rebounds': abstract_player.total_rebounds,
                                                                        'defensive_rebounds': abstract_player.defensive_rebounds,
                                                                        'offensive_rebounds': abstract_player.offensive_rebounds,
                                                                        'assists': abstract_player.assists,
                                                                        'steals': abstract_player.steals,
                                                                        'blocks': abstract_player.blocks,
                                                                        'turnovers': abstract_player.turnovers,
                                                                        'personal_fouls': abstract_player.personal_fouls,
                                                                        'points': abstract_player.points,
                                                                        'true_shooting_percentage': abstract_player.true_shooting_percentage,
                                                                        'free_throw_attempt_rate': abstract_player.free_throw_attempt_rate,
                                                                        'three_point_attempt_rate': abstract_player.three_point_attempt_rate,
                                                                        'total_rebound_percentage': abstract_player.total_rebound_percentage,
                                                                        'defensive_rebound_percentage': abstract_player.defensive_rebound_percentage,
                                                                        'offensive_rebound_percentage': abstract_player.offensive_rebound_percentage,
                                                                        'assist_percentage': abstract_player.assist_percentage,
                                                                        'steal_percentage': abstract_player.steal_percentage,
                                                                        'block_percentage': abstract_player.block_percentage,
                                                                        'turnover_percentage': abstract_player.turnover_percentage,
                                                                        'usage_percentage': abstract_player.usage_percentage})
            player_dict = player.dataframe.to_dict('records')[0]
            player_dict['game'] = game
            PlayerBoxscore.objects.update_or_create(Player=model_player, date=boxscore.date, defaults=player_dict)
            input(player._player_id)
            player_dict = player.dataframe.to_dict('records')[0]
            input(player_dict)
