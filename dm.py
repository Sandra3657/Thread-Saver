import tweepy
import os
  

def send_threads(threads):
# assign the values accordingly
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_KEY_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    
    for thread in threads:
    # authorization of consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        # set access to user's access key and access secret 
        auth.set_access_token(access_token, access_token_secret)
        
        # calling the api 
        api = tweepy.API(auth)
        print(api)

        #sending direct message
        recipient_id = thread['id']  # ID of the user
        api.send_direct_message(recipient_id, thread['text'])