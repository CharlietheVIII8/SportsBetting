from django.core.management.base import BaseCommand, CommandError
from SportsBetting.settings import TWITTER_ACCESS_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_TOKEN_SECRET
from ...models import TwitterAccount, Tweet
from datetime import datetime
import tweepy as tw


class Command(BaseCommand):
    help = 'Get tweets'

    def handle(self, *args, **options):
        auth = tw.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_TOKEN_SECRET)
        api = tw.API(auth, wait_on_rate_limit=True)
        accounts = TwitterAccount.objects.all()
        for account in accounts:
            tweets = api.user_timeline(screen_name=account.handle,
                                       count=200,
                                       include_rts=True,
                                       tweet_mode='extended')
            for tweet in tweets:
                tweet_dict = tweet.__dict__['_json']
                date = datetime.strptime(tweet_dict['created_at'], '%a %b %d %H:%M:%S %z %Y')
                Tweet.objects.update_or_create(id=str(tweet_dict['id']), account=account, defaults={'created_at': date,
                                                                                                    'full_text':
                                                                                                        tweet_dict[
                                                                                                            'full_text'],
                                                                                                    'in_reply_to_status_id': str(
                                                                                                        tweet_dict[
                                                                                                            'in_reply_to_status_id']),
                                                                                                    'in_reply_to_user_id': str(
                                                                                                        tweet_dict[
                                                                                                            'in_reply_to_user_id']),
                                                                                                    'in_reply_to_screen_name':
                                                                                                        tweet_dict[
                                                                                                            'in_reply_to_screen_name'],
                                                                                                    'retweet_count':
                                                                                                        tweet_dict[
                                                                                                            'retweet_count'],
                                                                                                    'favorite_count':
                                                                                                        tweet_dict[
                                                                                                            'favorite_count']})
