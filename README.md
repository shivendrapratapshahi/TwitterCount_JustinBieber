# Data Pipeline for TwitterCount_JustinBieber

##Steps for the Solution
Created a Twitter account and API credentials
Downloade any opensource Database - Decided to download MySQL database because of it's widespread use
Install the Tweepy and mysql-connector Python Libraries
After looking at the twitter documentation, I found the most important and useful fields to extract for our dataset from the twitter API: username, created_at, tweet, retweet_count and location of the tweet.
I created an object for my class 'StdOutListener' and extracted all the tweets from the API with the filter '#justinbieber' in it.
Before storing it in my database, I implemented a few checks:
Kept a track of Number of tweets: tweetCount
Filtering out duplicate tweet by initialising a list and checking if the tweet has already been consumed.
Since the previous step has been executed, Number of tweets and Number of unique tweets will remain same.
I'm also filtering out on the keyword '#music' or 'music'.
Final step is to store the tweet and it's related information in the database.
