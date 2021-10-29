import tweepy
import sentence_generator
from os import environ

def main():
    consumer_key = environ['CONSUMER_KEY']
    consumer_secret = environ['CONSUMER_SECRET']
    access_token = environ['ACCESS_TOKEN']
    access_token_secret = environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.me()

    sentence = sentence_generator.generate_random_sentence()

    print(sentence)
    
    assert len(sentence)<=280

    api.update_status(sentence)

if __name__ == '__main__':
    main()