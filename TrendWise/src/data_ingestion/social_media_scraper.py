import tweepy
from TrendWise.src.config import TWITTER_API_KEY, TWITTER_API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

def get_twitter_trends():
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    trends = api.get_place_trends(id=23424977)  # ID de EE.UU.
    return [trend["name"] for trend in trends[0]["trends"]]

