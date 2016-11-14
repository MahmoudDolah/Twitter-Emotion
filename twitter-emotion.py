#! /usr/bin/python3
from __future__ import print_function
from textblob import TextBlob
import tweepy
import auth_keys # This is the file that stores your authentication keys


class Tweet:
    def __init__(self, txt, pol, sub):
        self.text = txt
        self.polarity = pol
        self.subjectivity = sub
        # polarity goes from -1 to 1, subjectivity goes from 0 to 1 (objective to opinionated)

    def display(self):
        '''Displays the text, polarity and subjectivity of the tweet'''
        print(self.text)
        print("Polarity: " + str(self.polarity) + ", " + "Subjectivity: " + str(self.subjectivity))
        print("\n")

def search(api, search_term):
    public_tweets = api.search(search_term)
    tweets = []
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        twt = Tweet(tweet.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity)
        twt.display()
        tweets.append(twt)
        print("")
    return tweets

def average_rating(tweets):
    sum_polarity = 0
    sum_subjectivity = 0
    for tweet in tweets:
        sum_polarity += tweet.polarity
        sum_subjectivity += tweet.subjectivity
    avg_polarity = sum_polarity/len(tweets)
    avg_subjectivity = sum_subjectivity/len(tweets)
    return avg_polarity, avg_subjectivity

def main():
    auth = tweepy.OAuthHandler(auth_keys.consumer_key, auth_keys.consumer_secret)
    auth.set_access_token(auth_keys.access_token, auth_keys.access_token_secret)

    api = tweepy.API(auth)

    search_term = input("Enter term to search: ")
    tweets = search(api, search_term)
    avg_polarity, avg_subjectivity = average_rating(tweets)
    print("Sentiment Analysis for: " + search_term)
    print("Average Polarity of Tweets: " + str(avg_polarity) +".")
    print("Average Subjectivity of Tweets: " + str(avg_subjectivity) +".")

if __name__ == "__main__":
    main()
    