import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return os.getenv("BEARER_TOKEN")


def create_url(username):
    url = "https://api.twitter.com/2/users/by/username/{}".format(username)
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    print(response)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()
    # return response


def get_user_id(username):
    bearer_token = auth()
    url = create_url(username)
    headers = create_headers(bearer_token)
    json = connect_to_endpoint(url, headers)
    if 'errors' in json:
        return None
    # json = response.json()
    print(json)
    id = json['data']['id']
    return int(id)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

# print(get_user_id("645"))
