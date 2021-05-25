![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Threadify

A twitter bot that sends threads of a tweet as dm to the users who mentioned it .

## Installation

### Clone project

`git clone https://github.com/Sandra3657/Threadify.git`\
`cd Treadify`

### Create virtual environment

For windows: `py -3 -m venv venv` \
For linux: `python3 -m venv venv`

### Activate venv

For windows: `venv\Scripts\activate`\
For linux: `. venv/bin/activate`

### Install packages
`pip install -r requirements.txt

## Link to product walkthrough
[link to video]
## How it Works ?
The bot checks for mentions from users. From the mentioned tweet the bot takes the conversation id of the entire thread. Conversation id is same for tweets in a particular thread. Then using conversation id we get the entire thread and avoid the replies from other users so as to get the tweets from the tweet author only . Then those threads will be send as DMs to corresponding user who tagged the bot.
## Libraries used
astroid==2.5.6
certifi==2020.12.5
chardet==4.0.0
colorama==0.4.4
idna==2.10
isort==5.8.0
lazy-object-proxy==1.6.0
mccabe==0.6.1
oauthlib==3.1.0
pylint==2.8.2
PySocks==1.7.1
python-dotenv==0.17.1
requests==2.25.1
requests-oauthlib==1.3.0
six==1.16.0
toml==0.10.2
tweepy==3.10.0
urllib3==1.26.4
wrapt==1.12.1

## How to configure
Instructions for setting up project

## How to Run
Instructions for running

##Team Members
1.Sandra Kakkarayil Jayakumar[https://github.com/Sandra3657]  
2.Parvathy P[https://github.com/parvathyp301]
3.Akshaya Thomas[https://github.com/akshayathomas2001]

##Team ID
BFH/recANMvYohi0GiMRj/2021
