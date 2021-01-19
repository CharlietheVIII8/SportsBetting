from django.core.management.base import BaseCommand, CommandError
from sportsipy.ncaab.teams import Teams
from ...models import Team


class Command(BaseCommand):
    help = 'Get teams'

    def handle(self, *args, **options):
        teams = Teams()
        for team in teams:
            team_dict = team.dataframe.to_dict('records')[0]
            Team.objects.update_or_create(abbreviation=team_dict['abbreviation'],
                                          name=team_dict['name'],
                                          defaults={'minutes_played': team_dict['minutes_played'],
                                                    'field_goals_made': team_dict['field_goals'],
                                                    'field_goals_attempted': team_dict['field_goal_attempts'],
                                                    'field_goal_percentage': team_dict['field_goal_percentage'],
                                                    'three_pointers_made': team_dict['three_point_field_goals'],
                                                    'three_pointers_attempted': team_dict[
                                                        'three_point_field_goal_attempts'],
                                                    'three_point_percentage': team_dict[
                                                        'three_point_field_goal_percentage'],
                                                    'two_pointers_made': team_dict['two_point_field_goals'],
                                                    'two_point_percentage': team_dict[
                                                        'two_point_field_goal_percentage'],
                                                    'two_pointers_attempted': team_dict[
                                                        'two_point_field_goal_attempts'],
                                                    'effective_field_goal_percentage': team_dict[
                                                        'effective_field_goal_percentage'],
                                                    'free_throws_made': team_dict['free_throws'],
                                                    'free_throw_percentage': team_dict['free_throw_percentage'],
                                                    'free_throws_attempted': team_dict['free_throw_attempts'],
                                                    'total_rebounds': team_dict['total_rebounds'],
                                                    'defensive_rebounds': team_dict['defensive_rebounds'],
                                                    'offensive_rebounds': team_dict['offensive_rebounds'],
                                                    'assists': team_dict['assists'],
                                                    'steals': team_dict['steals'],
                                                    'blocks': team_dict['blocks'],
                                                    'turnovers': team_dict['turnovers'],
                                                    'personal_fouls': team_dict['personal_fouls'],
                                                    'points': team_dict['points'],
                                                    'true_shooting_percentage': team_dict['true_shooting_percentage'],
                                                    'free_throw_attempt_rate': team_dict['free_throw_attempt_rate'],
                                                    'three_point_attempt_rate': team_dict['three_point_attempt_rate'],
                                                    'total_rebound_percentage': team_dict['total_rebound_percentage'],
                                                    'offensive_rebound_percentage': team_dict[
                                                        'offensive_rebound_percentage'],
                                                    'assist_percentage': team_dict['assist_percentage'],
                                                    'steal_percentage': team_dict['steal_percentage'],
                                                    'block_percentage': team_dict['block_percentage'],
                                                    'turnover_percentage': team_dict['turnover_percentage'],
                                                    'away_losses': team_dict['away_losses'],
                                                    'away_wins': team_dict['away_wins'],
                                                    'conference': team_dict['conference'],
                                                    'games_played': team_dict['games_played'],
                                                    'losses': team_dict['losses'],
                                                    'wins': team_dict['wins'],
                                                    'free_throws_per_field_goal_attempt': team_dict[
                                                        'free_throws_per_field_goal_attempt'],
                                                    'net_rating': team_dict['net_rating'],
                                                    'offensive_rating': team_dict['offensive_rating'],
                                                    'opp_assist_percentage': team_dict['opp_assist_percentage'],
                                                    'opp_assists': team_dict['opp_assists'],
                                                    'opp_block_percentage': team_dict['opp_block_percentage'],
                                                    'opp_blocks': team_dict['opp_blocks'],
                                                    'opp_defensive_rebounds': team_dict['opp_defensive_rebounds'],
                                                    'opp_effective_field_goal_percentage': team_dict[
                                                        'opp_effective_field_goal_percentage'],
                                                    'opp_field_goal_attempts': team_dict['opp_field_goal_attempts'],
                                                    'opp_field_goal_percentage': team_dict['opp_field_goal_percentage'],
                                                    'opp_field_goals_made': team_dict['opp_field_goals'],
                                                    'opp_free_throw_attempt_rate': team_dict[
                                                        'opp_free_throw_attempt_rate'],
                                                    'opp_free_throw_attempts': team_dict['opp_free_throw_attempts'],
                                                    'opp_free_throw_percentage': team_dict['opp_free_throw_percentage'],
                                                    'opp_free_throws_made': team_dict['opp_free_throws'],
                                                    'opp_free_throws_per_field_goal_attempt': team_dict[
                                                        'opp_free_throws_per_field_goal_attempt'],
                                                    'opp_offensive_rating': team_dict['opp_offensive_rating'],
                                                    'opp_offensive_rebound_percentage': team_dict[
                                                        'opp_offensive_rebound_percentage'],
                                                    'opp_offensive_rebounds': team_dict['opp_offensive_rebounds'],
                                                    'opp_personal_fouls': team_dict['opp_personal_fouls'],
                                                    'opp_points': team_dict['opp_points'],
                                                    'opp_steal_percentage': team_dict['opp_steal_percentage'],
                                                    'opp_steals': team_dict['opp_steals'],
                                                    'opp_three_point_attempt_rate': team_dict[
                                                        'opp_three_point_attempt_rate'],
                                                    'opp_three_point_field_goal_attempts': team_dict[
                                                        'opp_three_point_field_goal_attempts'],
                                                    'opp_three_point_field_goal_percentage': team_dict[
                                                        'opp_three_point_field_goal_percentage'],
                                                    'opp_three_point_field_goals_made': team_dict[
                                                        'opp_three_point_field_goals'],
                                                    'opp_two_point_field_goal_attempts': team_dict[
                                                        'opp_two_point_field_goal_attempts'],
                                                    'opp_two_point_field_goal_percentage': team_dict[
                                                        'opp_two_point_field_goal_percentage'],
                                                    'opp_two_point_field_goals_made': team_dict[
                                                        'opp_two_point_field_goals'],
                                                    'opp_total_rebound_percentage': team_dict[
                                                        'opp_total_rebound_percentage'],
                                                    'opp_total_rebounds': team_dict['opp_total_rebounds'],
                                                    'opp_true_shooting_percentage': team_dict[
                                                        'opp_true_shooting_percentage'],
                                                    'opp_turnover_percentage': team_dict['opp_turnover_percentage'],
                                                    'opp_turnovers': team_dict['opp_turnovers'],
                                                    'pace': team_dict['pace'],
                                                    'simple_rating_system': team_dict['simple_rating_system'],
                                                    'strength_of_schedule': team_dict['strength_of_schedule'],
                                                    'win_percentage': team_dict['win_percentage']})
