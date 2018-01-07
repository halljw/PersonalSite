#!/usr/bin/env python

import twitter

class Twitter_Searcher:

  def __init__(self):
    self.get_credentials()

  def get_credentials(self):
    """
    Gets authorization credentials from 'credentials.txt'
    Should be run upon construction in order to use credentials
     when authorizing use of twitter api.
    """
    cred_file = 'credentials.txt'
    try:
      f = open(cred_file, 'r')
    except IOError:
      print("[-] File '%s' not found\n[-] Run 'authorize.py' to generate credentials" % cred_file)
      exit()
    except:
      print("[-] Unknown error while reading credentials from '%s'" % cred_file)
      exit()

    try:
      self.app_name = f.readline().split(':')[1].strip()
      self.consumer_key = f.readline().split(':')[1].strip()
      self.consumer_secret = f.readline().split(':')[1].strip()
      self.access_key = f.readline().split(':')[1].strip()
      self.access_secret = f.readline().split(':')[1].strip()
    except:
      print("[-] Issue while reading credentials\n[-] Run 'authorize.py to generate credentials")
      exit()

  def get_tweets(self, search_term, count=15):
    """
    Conducts key-word search of twitter for 'search_term'
    Number of returned tweets must be <= 100. Searchs for 1 by default.
    If exceeding max number of queries (15 queries per 15 minute period) or if
      tweet fails to load, use default tweet as placeholder.
    """
    try:
      t = twitter.Twitter(auth = twitter.OAuth(
        self.access_key, 
        self.access_secret, 
        self.consumer_key, 
        self.consumer_secret))

    except:
      print('[-] Error when authorizing twitter API. Remember: 15 queries per 15 minute-period')

    try:
      query = t.search.tweets(q=search_term, count=count)	# conduct twitter seach
      tweets = [hit['text'] for hit in query['statuses']]
      for tweet in tweets:
        print(tweet + "\n")

    except IndexError:
      print('[-] Query did not return results. Retry query.')







if __name__=='__main__':
  ts = Twitter_Searcher()
  ts.get_tweets("breath of the wild")

