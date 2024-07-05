#use v2 API version 

from requests_oauthlib import OAuth1Session
import json
import time
import os
import schedule
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

consumer_key =os.getenv('API_KEY')
consumer_secret = os.getenv('API_KEY_SECRET')

# File to store access tokens
TOKEN_FILE = "twitter_tokens.json"

def get_oauth_session():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
        access_token = tokens['access_token']
        access_token_secret = tokens['access_token_secret']
    else:
        # Get request token
        request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)
        
        try:
            fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError:
            print("There may have been an issue with the consumer_key or consumer_secret you entered.")
            return None

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

        # Get authorization
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        # Save tokens
        with open(TOKEN_FILE, 'w') as f:
            json.dump({
                'access_token': access_token,
                'access_token_secret': access_token_secret
            }, f)

    return OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

def post_tweet(oauth_session):
    # You can modify this function to generate different tweet content each time
    payload = {"text": f"Automated tweet at {time.strftime('%Y-%m-%d %H:%M:%S')}"}

    try:
        response = oauth_session.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            print(f"Request returned an error: {response.status_code} {response.text}")
        else:
            print("Tweet posted successfully")
            print(json.dumps(response.json(), indent=4, sort_keys=True))
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    oauth_session = get_oauth_session()
    if oauth_session is None:
        return

    # Schedule the tweet to be posted every 2 hours
    schedule.every(2).hours.do(post_tweet, oauth_session)

    print("Bot is running. Press Ctrl+C to stop.")
    while True:
        # post_tweet(oauth_session)
        # time.sleep(60)
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()