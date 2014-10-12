#!/usr/bin/env python
# encoding: utf-8
"""
TwitterStream.py

Created by Sree Nilakanta on 2014-10-11.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib.pyplot as plt

import re

#Variables that contains the user credentials to access Twitter API 
access_token = "23819877-DR01utygKD9FYc4vKd7lrDivDkCuvgiU1yd9snuTS"
access_token_secret = "sEoyFPlJalZn8WPaPqwJAkCWLDkgJLGsStCmDTzzRYCKr"
consumer_key = "bkKprvopmc6GfGjRadmOXIOHG"
consumer_secret = "sQTvjqyFskDp2aCEsSnANAZxPsPnVfxVM6D3fcSumZQPHB9AJP"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

#read  data into an array for use as dataframe 	
	def make_twtarray():
		
		tweets_data_path = '../data/twitter_data.txt'

		tweets_data = []
		tweets_file = open(tweets_data_path, "r")
		for line in tweets_file:
		    try:
		        tweet = json.loads(line)
		        tweets_data.append(tweet)
		    except:
		        continue
		print len(tweets_data
		)
#create a dataframe in Pandas
	def make_twdf():
		tweets = pd.DataFrame()
		#add three columns
		tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
		tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
		tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
		
#Make two charts of the data
	def make_chartLang()::
		tweets_by_lang = tweets['lang'].value_counts()

		fig, ax = plt.subplots()
		ax.tick_params(axis='x', labelsize=15)
		ax.tick_params(axis='y', labelsize=10)
		ax.set_xlabel('Languages', fontsize=15)
		ax.set_ylabel('Number of tweets' , fontsize=15)
		ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
		tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
		
	def make_chartCountry():
		tweets_by_country = tweets['country'].value_counts()

		fig, ax = plt.subplots()
		ax.tick_params(axis='x', labelsize=15)
		ax.tick_params(axis='y', labelsize=10)
		ax.set_xlabel('Countries', fontsize=15)
		ax.set_ylabel('Number of tweets' , fontsize=15)
		ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
		tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
#Check for keywords		
		def word_in_text(word, text):
		    word = word.lower()
		    text = text.lower()
		    match = re.search(word, text)
		    if match:
		        return True
		    return False
		#add three new columns
			tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
			tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
			tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))
		#print the number of entries
			print tweets['python'].value_counts()[True]
			print tweets['javascript'].value_counts()[True]
			print tweets['ruby'].value_counts()[True]
		#plot the comparative chart
			x_pos = list(range(len(prg_langs)))
			width = 0.8
			fig, ax = plt.subplots()
			plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

		# Setting axis labels and ticks
			ax.set_ylabel('Number of tweets', fontsize=15)
			ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
			ax.set_xticks([p + 0.4 * width for p in x_pos])
			ax.set_xticklabels(prg_langs)
			plt.grid()
			
		def rel_tweets():
			tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
			tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
			
			tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))
			print tweets['programming'].value_counts()[True]
			print tweets['tutorial'].value_counts()[True]
			print tweets['relevant'].value_counts()[True]
			
			print tweets[tweets['relevant'] == True]['python'].value_counts()[True]
			print tweets[tweets['relevant'] == True]['javascript'].value_counts()[True]
			print tweets[tweets['relevant'] == True]['ruby'].value_counts()[True]
			
		#Extract links of tutorial
			def extract_link(text):
			    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
			    match = re.search(regex, text)
			    if match:
			        return match.group()
			    return ''
			
			tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
			tweets_relevant = tweets[tweets['relevant'] == True]
			tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']
			
			print tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link']
			print tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link']
			print tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link']
			

			
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])


