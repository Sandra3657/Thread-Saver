import tweepy
  
# assign the values accordingly
consumer_key = "consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access token secret"
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)

#To get ID of user
user = api.get_user("username")
print(user.id_str)

#sending direct message
recipient_id = "id_of_user"  # ID of the user
api.send_direct_message(recipient_id, "Hi")
