# import requests
# import os
# import json
# import string
# import secrets
# import time
# from requests_oauthlib import OAuth1

# url =  "https://api.twitter.com/1.1/direct_messages/events/new.json"

# oauth_consumer_key = os.environ.get("CONSUMER_KEY")
#     oauth_token = os.environ.get("ACCESS_TOKEN")
#     nonce = generate_token()
#     signature = ""
#     timestamp = time.time()

# auth = OAuth1(resource_owner_key = )


# # def auth():
# #     return os.environ.get("BEARER_TOKEN")


# # curl --request POST 
# # --url https://api.twitter.com/1.1/direct_messages/events/new.json 
# # --header 'authorization: OAuth oauth_consumer_key="YOUR_CONSUMER_KEY", oauth_nonce="AUTO_GENERATED_NONCE", oauth_signature="AUTO_GENERATED_SIGNATURE", oauth_signature_method="HMAC-SHA1", oauth_timestamp="AUTO_GENERATED_TIMESTAMP", oauth_token="USERS_ACCESS_TOKEN", oauth_version="1.0"' 
# # --header 'content-type: application/json' 
# # --data '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "RECIPIENT_USER_ID"}, "message_data": {"text": "Hello World!"}}}}'


# def generate_token():
#     alphabet = string.ascii_letters + string.digits
#     token = ''.join(secrets.choice(alphabet) for i in range(32))
#     return token

# def create_url():
#     # Replace with user ID below
#     return "https://api.twitter.com/1.1/direct_messages/events/new.json "


# def get_params():
#     return {}




# def create_headers():
#     oauth_consumer_key = os.environ.get("CONSUMER_KEY")
#     oauth_token = os.environ.get("ACCESS_TOKEN")
#     nonce = generate_token()
#     signature = ""
#     timestamp = time.time()

#     headers = {"authorization": 'OAuth oauth_consumer_key={}, oauth_nonce={}, oauth_signature={}, oauth_signature_method="HMAC-SHA1", oauth_timestamp={},oauth_token={}, oauth_version="1.0"'.format(oauth_consumer_key,nonce, signature,timestamp,oauth_token)}
#     return headers


# def connect_to_endpoint(url, headers, params):
#     response = requests.request("POST", url, headers=headers, params=params)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(
#             "Request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     return response.json()

# # def get_data(user_id, since_id):
# #     dict = []
# #     # bearer_token = auth()
    
# #     result_count = json_response['meta']['result_count']
# #     # since_id  = json_response['meta']['newest_id']
# #     if result_count == 0:
# #         # time.sleep(60)
# #         # print("No results")
# #         return (since_id,dict)
# #     since_id  = json_response['meta']['newest_id']
# #     data = json_response['data']
# #     for tweet in data:
# #         if tweet.get('in_reply_to_user_id'):
# #             dict.append({'id': tweet['author_id'], 'conversation_id': tweet['conversation_id'], 'in_reply_to_user_id': tweet['in_reply_to_user_id']})
# #     return (since_id,dict)


# def main():
#     url = create_url()
#     headers = create_headers()
#     params = get_params()
#     json_response = connect_to_endpoint(url, headers, params)
#     print(json.dumps(json_response, indent=4, sort_keys=True))       

# # if __name__ == '__main__':
# #     main()


  
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