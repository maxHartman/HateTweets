"""
Authors: Max Hartman, Alexis Mitchnick, Sarah Raizen
Date: December 2019

This is for a Twitter Hate Speech project, so the incoming content is in 
un-indexed, un-headered csv files with the first column having the tweet_id
and the second having a label (in most cases 'hate' or 'not hate'). The
contents of this column are not particulary relevant here, but they are
accessed.

The code is built on top of the Tweepy API. Documentation on the API and 
its functionality can be found here: https://tweepy.readthedocs.io/
"""

import pandas as pd
import csv
from math import floor, ceil
from tweepy import OAuthHandler, Stream, API, TweepError

def get_tweets(content, API):
	"""
	Get raw Tweets via the API with only tweet_ids.

	Arguments
	----------
	content : [[str, str]]
		A list of 2-element lists of [tweet_id, label]
	API : API()
		The api created to access Twitter data

	Returns
	-------
	full_entries : [[str, str, str]]
		A list of 3-element lists of [tweet_id, tweet_text, label]
	"""

	# twitter only allows for 100 Tweets in the status_lookup function
	MAX_TWEETS_PER_ITERATION = 100
	iterations = ceil(len(content)/MAX_TWEETS_PER_ITERATION)

	full_entries = []

	# put the content array into a dictionary for faster lookup 
	content_dict = {entry[0]: entry[1] for entry in content}

	for i in range(iterations):
		start_idx = i * MAX_TWEETS_PER_ITERATION
		end_idx = min(start_idx + MAX_TWEETS_PER_ITERATION, len(content)) - 1

		# gets a list of just the tweet_ids (without the labels)
		curr_content = content[start_idx:end_idx]
		tweet_ids = __get_tweet_ids(curr_content)
		
		# get raw tweets of the 100 tweet_ids in this batch
		pulled_ids_and_tweets = get_statuses(tweet_ids, API)

		for t_id, raw_tweet in pulled_ids_and_tweets:
			label = content_dict[t_id]
			full_entries.append([t_id, raw_tweet, label])

	return full_entries


def __get_tweet_ids(content):
	""" 
	Pull out the [tweet_id]s given the specified format mentioned at the 
	top of the file.
	"""

	tweet_ids = []
	for i in range(len(content)):
		# just append the tweet id element (excludes the label)
		tweet_ids.append(content[i][0])
	return tweet_ids

def get_statuses(tweet_ids, API):
	"""
	Retrieve status objects from tweet_ids via the API. 

	This function makes use of the statuses_lookup() function, which, by
	default, does not throw an error if a tweet_id in the list does not / 
	no longer maps to an available status. A status is all of the available 
	data for one Tweet.
	"""

	statuses = API.statuses_lookup(tweet_ids)
	return [(tweet.id_str, tweet.text) for tweet in statuses]

def get_status(tweet_id, API):
	"""
	Retrieve status object from a single tweet_id via the API. 

	This function makes use of the get)status() function, which, by
	default, does throw an error if the tweet_id does not / no longer
	maps to an available status.
	"""

	status = API.get_status(tweet_id)
	return (status.id_str, status.text)


def read_csv(fp_in):
	""" Read CSV file and return a list of lists. """

	entries = []
	with open(fp_in, 'r', newline='') as file_in:
		file_reader = csv.reader(file_in)
		for row in file_reader:
			entries.append(row)
	return entries

def write_csv(fp_out, content):
	""" Write CSV file from content list to filepath. """

	with open(fp_out, 'w', newline='') as file_out:
		file_writer = csv.writer(file_out)
		file_writer.writerows(content)
	return


def main(fp_in, fp_out, API):
	entries = read_csv(fp_in)
	final_content = get_tweets(entries, API)
	write_csv(fp_out, final_content)
	return


if __name__== "__main__":
	from twitter_credentials import CONSUMER_KEY, CONSUMER_SECRET, \
		ACCESS_TOKEN, ACCESS_TOKEN_SECRET

	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = API(auth)

	main('NAACL_SRW_2016.csv', 'NAACL_SRW_2016_with_tweets.csv', api)
