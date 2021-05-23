import requests
import os
import json
import time

def auth():
    return os.environ.get("BEARER_TOKEN")


def create_url(ref_id, author_id,main_tweet = False):
    # Replace with user ID below
    # user_id = 2244994945
    # if since_id is None:
    #     return "https://api.twitter.com/2/users/{}/mentions?max_results=5".format(user_id)
    # return "https://api.twitter.com/2/users/{}/mentions?max_results=5&since_id={}".format(user_id, since_id)
    # ref_id = "1394971601045700612"
    # author_id = "905404575267639296"
    if main_tweet:
        return "https://api.twitter.com/2/tweets/{}".format(ref_id)
    return "https://api.twitter.com/2/tweets/search/recent?query=conversation_id:{}%20from%3A{}&max_results=50".format(ref_id, author_id)

def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at,conversation_id", "expansions":"in_reply_to_user_id,author_id"}


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


def get_thread(dict):
    threads = []
    for item in dict:
        thread = {}
        bearer_token = auth()
        headers = create_headers(bearer_token)
        params = get_params()
        conversation_id = item['conversation_id']
        in_reply_to_user_id = item['in_reply_to_user_id']
        thread['id'] = item['id']
        thread['text'] = ""

        main_tweet_url = create_url(conversation_id, in_reply_to_user_id, True)
        main_tweet_json_response = connect_to_endpoint(main_tweet_url, headers, params)
        main_tweet  = main_tweet_json_response['data']['text']
        # thread = [main_tweet]
        thread['text'] = main_tweet + "\n"

        url = create_url(conversation_id, in_reply_to_user_id)
        json_response = connect_to_endpoint(url, headers, params)
        print(json.dumps(json_response, indent=4, sort_keys=True))
        result_count = json_response['meta']['result_count']
        if result_count > 0:
            text_list = []
            data = list(reversed(json_response['data']))
            # thread.append(tweet['text'] for tweet in data)
            for tweet in data:
                text_list.append(tweet['text'])
            # rev_thread = list(reversed(thread))
            print(thread['text']+"\n".join(text_list))
            thread['text'] = thread['text'] + "\n".join(text_list)
        threads.append(thread)
    return threads


# def main():
    
#     # url = create_url("1394971601045700612", "905404575267639296")
#     get_thread([{'conversation_id': "1394971601045700612", 'in_reply_to_user_id': "905404575267639296"}])
    


# {"data":[{"conversation_id":"1395417996382851080","id":"1395417996382851080","text":"RT @WhatIsStoicism: ⏳\n\"While we are postponing, \n\nlife speeds by.\"\n\n- Seneca's Letters: 1. On Saving Time\nhttps://t.co/KS6p6lNEsD"},{"conversation_id":"1395403321092067328","id":"1395403321092067328","text":"RT @peternlimberg: I had fun hosting a really fun salon at @TheAnnaGat's @interintellect_ yesterday. It was called ...\n\nWill Stoicism Save…"},{"conversation_id":"1395401429821497345","id":"1395401429821497345","text":"\uD835\uDDE3\uD835\uDDF5\uD835\uDDF6\uD835\uDDF9\uD835\uDDFC\uD835\uDE00\uD835\uDDFC\uD835\uDDFD\uD835\uDDF5\uD835\uDE06\n\nfrom Greek: philosophia = 'love of wisdom'\nhttps://t.co/f2mohNbVUg"},{"conversation_id":"1395394266646654978","id":"1395394266646654978","text":"RT @WhatIsStoicism: #Stoicism #Wallpaper \uD83D\uDCF1\uD83E\uDD33 https://t.co/pq4WA7fBP9"},{"conversation_id":"1395313346987970563","id":"1395390102810079232","text":"For more comics and other Stoic snippets check out the the WIS weekly email \uD83D\uDE42:\n\nhttps://t.co/hYmr7PiC2u"},{"conversation_id":"1395379133778169858","id":"1395379133778169858","text":"“Suppose, for example, that in talking to an athlete, I said, “Show me your shoulders,” and then he answered, “Look at my weights.” \n\nGet out of here with you and your weights! \n\nWhat I want to see is how you’ve profited from using the weights.”\n\n– Epictetus, Discourses 1.4.13 https://t.co/Q5pdNJ0EIt"},{"conversation_id":"1395374354612035588","id":"1395374354612035588","text":"You don’t need to have a near-death experience\n\nto consider yourself “lucky to be alive.”"},{"conversation_id":"1395359733771558916","id":"1395368656142544897","text":"@DonJRobertson @Justahalfforme Enjoyed this one, are there any new episodes in the works?"},{"conversation_id":"1395360413261443082","id":"1395360413261443082","text":"RT @WhatIsStoicism: DOING good leads to\n\nBEING good leads to\n\nHAVING good days."},{"conversation_id":"1395313346987970563","id":"1395313346987970563","text":"Stoic Comic:\nControlling the passage of time... https://t.co/WokfT6MF3U"}],"meta":{"oldest_id":"1395313346987970563","newest_id":"1395417996382851080","result_count":10,"next_token":"7140dibdnow9c7btw3w4sgjnsn85stb3sskmieprvodo3"}}
           


    

# if __name__ == "__main__":
#     main()