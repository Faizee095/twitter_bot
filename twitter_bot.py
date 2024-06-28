import tweepy
import schedule
import time
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

# Step 1: Authenticate to Twitter
def authenticate_twitter():
    api_key =  os.getenv('API_KEY')
    print(api_key)
    api_secret_key =  os.getenv('API_KEY_SECRET')
    access_token =  os.getenv('ACCESS_TOKEN')
    access_token_secret =  os.getenv('ACCESS_TOKEN_SECRET')
    
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

# Step 2: Define the post content
def create_post_content():
    # Customize your message or generate dynamically
    return "Hello, Twitter! This is an automated post every 2 hours."

# Step 3: Post the tweet
def post_tweet(api):
    content = create_post_content()
    try:
        api.update_status(content)
        print("Tweeted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Post a tweet immediately
def post_tweet_now():
    api = authenticate_twitter()
    post_tweet(api)

# Step 4: Schedule the post every 2 hours
def schedule_tweets():
    api = authenticate_twitter()
    schedule.every(2).hours.do(lambda: post_tweet(api))
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    post_tweet_now()
    schedule_tweets()

