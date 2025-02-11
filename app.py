import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

consumer_key = os.getenv("Consumer_Key")
consumer_secret = os.getenv("Consumer_Secret")
access_token = os.getenv("Access_Token")
access_secret = os.getenv("Access_Secret")

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret
)

print(client.search_recent_tweets(query="#stockmarketcrash", max_results=10))
