import requests
import os
import json
import time

def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(since_id):
    # Replace with user ID below
    user_id = 2244994945
    if since_id is None:
        return "https://api.twitter.com/2/users/{}/mentions?max_results=5".format(user_id)
    return "https://api.twitter.com/2/users/{}/mentions?max_results=5&since_id={}".format(user_id, since_id)


def get_params():
    return {"tweet.fields": "created_at,conversation_id,in_reply_to_user_id", "expansions":"in_reply_to_user_id,author_id"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def get_data(since_id, bearer_token):
    dict = []
    url = create_url(since_id)
    headers = create_headers(bearer_token)
    params = get_params()
    json_response = connect_to_endpoint(url, headers, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))       
    result_count = json_response['meta']['result_count']
    # since_id  = json_response['meta']['newest_id']
    if result_count == 0:
        # time.sleep(60)
        # print("No results")
        return (since_id,dict)
    since_id  = json_response['meta']['newest_id']
    data = json_response['data']
    for tweet in data:
        if tweet.get('in_reply_to_user_id'):
            dict.append({'id': tweet['author_id'], 'conversation_id': tweet['conversation_id'], 'in_reply_to_user_id': tweet['in_reply_to_user_id']})
    # print(dict)
    # i = i+1
    print('---------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------')
    # time.sleep(60)
    return (since_id,dict)


def main():
    dict = []
    bearer_token = auth()
    since_id = None
    i = 0
    while True:
        # dict = []
        since_id, dict = get_data(since_id, bearer_token)
        print(dict)
        
        time.sleep(30)


if __name__ == "__main__":
    main()