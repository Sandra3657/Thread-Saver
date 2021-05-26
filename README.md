![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Threadify

A twitter bot that sends threads of a tweet as dm to the users who mentioned it.

## How to use?
The user has to just mention **@threadifier** in any of the tweets of the thread. The tweets of the thread will be then compiled together and then sent as a DM to the user.

## How it Works ?
The bot checks for mentions from users. From the mentioned tweet the bot takes the conversation id of the entire thread. Conversation id is same for tweets in a particular thread. Then using conversation id we get the entire thread and avoid the replies from other users so as to get the tweets from the tweet author only . Then those threads will be send as DMs to corresponding user who tagged the bot.

## Team Members
1. Sandra Kakkarayil Jayakumar[https://github.com/Sandra3657]  
2. Parvathy P[https://github.com/parvathyp301]
3. Akshaya Thomas[https://github.com/akshayathomas2001]

## Team ID
BFH/recANMvYohi0GiMRj/2021

## Link to product walkthrough
[https://www.loom.com/share/78be470fe59c46e193dd672c42740296]

## How to configure for local development
Instructions for setting up project

### 1. Twitter Development Account
Create a twitteer developer account.

### 2. Clone project

`git clone https://github.com/Sandra3657/Threadify.git`\
`cd Treadify`

### 3.  Create virtual environment

For windows: `py -3 -m venv venv` \
For linux: `python3 -m venv venv`

### 4.  Activate venv

For windows: `venv\Scripts\activate`\
For linux: `. venv/bin/activate`

### 5.  Install required packages
Run `pip install -r requirements.txt`

### 6. Add the API keys and tokens
Create a `.env` file in the main directory.

Add in your twitter developer account credentials :

```
BEARER_TOKEN=<Your Bearer Token>
CONSUMER_KEY=<Your consumer API key>
CONSUMER_KEY_SECRET=<Your consumer API Secret key>
ACCESS_TOKEN=<Your Access Token>
ACCESS_TOKEN_SECRET=<Your Access Token Secret>
```

### 7. Run the project
Run `python3 main.py`


## Libraries used
- astroid==2.5.6
- certifi==2020.12.5
- chardet==4.0.0
- colorama==0.4.4
- idna==2.10
- isort==5.8.0
- lazy-object-proxy==1.6.0
- mccabe==0.6.1
- oauthlib==3.1.0
- pylint==2.8.2
- PySocks==1.7.1
- python-dotenv==0.17.1
- requests==2.25.1
- requests-oauthlib==1.3.0
- six==1.16.0
- toml==0.10.2
- tweepy==3.10.0
- urllib3==1.26.4
- wrapt==1.12.1


