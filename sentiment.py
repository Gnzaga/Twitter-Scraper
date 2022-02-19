from textblob import TextBlob
import sys

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import pycountry
import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
import twint
import pandas as pd

def getTweets(topic=None, limit=100, fname=None):
    topic = topic
    limit = limit
    fname = fname
    if(topic == None):
        raise Exception("No Topic Provided")
    if(fname == None):
        raise Exception("No Filename Provided")

    c = twint.Config()

    c.Search = [topic]

    c.Limit = limit
#maybe change later to allow for different output formats
    c.Store_csv = True

    c.Output = fname


def percentage(part, whole):
    return 100 * float(part) / float(whole)





#topic = input("ENTER TOPIC: ")

#limit = int(input("LIMIT FOR TWEETS :"))

#fname = input("filename[no filetype]") + ".csv"

#getTweets(topic, limit, fname)

class sentimentData:
    def __init__(self, fname):
        self.fname = fname
        self.neu = 0
        self.neg = 0
        self.pos = 0
        self.polarity = 0
        self.tweetCount = 0

        self.tweets = []
        self.posList = []
        self.negList = []
        self.posList = []
        self.f = pd.read_csv(fname)



    def generateValues(self, quiet = False):
        for i in range(0, int(len(self.f))):
            if(self.f['language'].get(i).__eq__("en")):
                tweet = self.f['tweet'].get(i)
            #print(tweet + "\n\n")
                analysis = TextBlob(tweet)

                score = SentimentIntensityAnalyzer().polarity_scores(tweet)

                if(quiet == False and float(score['neg']) > 0.5):
                    print(str(score) + "  ->  "  + tweet + "\n")
                    #print(str(i) + " -> " + str(score))

                self.tweets.append(tweet)
                self.posList.append(score['pos'])
                self.negList.append(score['neg'])
                self.posList.append(score['pos'])

                if(float(score['pos']) > float(score['neg']) and float(score['pos']) > float(score['neg'])):
                    self.pos = self.pos+1

                if(float(score['neu']) > float(score['pos']) and float(score['neu']) > float(score['neg'])):
                    self.neu = self.neu+1

                if(float(score['neg']) > float(score['neu']) and float(score['neg']) > float(score['pos'])):
                    self.neg = self.neg+1





def tweetSentiment(fname):

    tweets_all = pd.read_csv(fname)

    tweets = tweets_all['tweet']
    positive = 0
    negative = 0
    postral = 0
    polarity = 0
    tweet_list = []
    postral_list = []
    negative_list = []
    positive_list = []



    for i in range(0, int(len(tweets_all))):
        if(tweets_all['language'].get(i).__eq__("en")):
            tweet = tweets_all['tweet'].get(i)
        #print(tweet + "\n\n")
            analysis = TextBlob(tweet)

            score = SentimentIntensityAnalyzer().polarity_scores(tweet)


            tweet_list.append(tweet)
            postral_list.append(score['pos'])
            negative_list.append(score['neg'])
            positive_list.append(score['pos'])
            if(score['neg'] > 0.3):
                #print(str(score) + "  ->  "  + tweet)
                print(str(i) + " -> " + str(score))
