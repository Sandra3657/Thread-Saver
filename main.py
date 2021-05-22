from user import get_user_id
from stream import get_data
from thread import get_thread
import os
import time


def auth():
    return os.environ.get("BEARER_TOKEN")

def main():
    username = "threadifier"
    user_id = get_user_id(username)
    bearer_token = auth()
    since_id = None
    while True:
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        since_id, mentioned_tweets = get_data(user_id, since_id)
        print(mentioned_tweets)
        time.sleep(30)
        print('------------------------------------------------------------------------')
        threads = get_thread(mentioned_tweets)
        print(threads)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')



        time.sleep(30)


if __name__ == '__main__':
    main()


