#Import the necessary methods from tweepy library
import nltk
nltk.download('punkt')
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
import json
from dateutil import parser
import time
import mysql.connector
from mysql.connector import Error

# Enter Twitter API Keys here
access_token = "please enter the access_token"
access_token_secret = "please enter the access_token_secret"
consumer_key = "please enter the consumer_key"
consumer_secret = "please enter the consumer_secret"
tracklist = ['#justinbieber'] #specifying the keyword 'justinbieber'
tweetChecklist = [];
tweetCount = 0 # Counter for number of tweets


def connect(created_at, tweet, username, location, retweet):
    """
    connect to MySQL database and insert twitter data
    """
    tweetCount = 0
    try:
        con = mysql.connector.connect(host = 'localhost',
        database='TwitterSchema', user='root', password = 'pl enter the password', charset = 'utf8')
        #print("connected to database")
        tweetCount += 1
        print ("The No. of tweets: %d " % (tweetCount) )
        

        if con.is_connected():
            """
            Insert twitter data
            """
            cursor = con.cursor()
            query = "insert into TwitterData (created_at, tweet, username,  location, retweet) values (%s, %s, %s, %s, %s)"
            cursor.execute(query, (created_at, tweet, username, location, retweet))
            con.commit()
            
            
    except Error as e:
        print(e)

    cursor.close()
    con.close()

    return



# Creating class for handling the twitter stream
class StdOutListener(StreamListener):

    def on_connect(self):
        print("Connection to Twitter API established")


    def on_error(self, status_code):
        if status_code != 200:
            print("error found")
            # returning false will disconnect the stream
            return False
      
    def on_data(self,data):
        
        try:
            raw_data = json.loads(data)
            if 'text' in raw_data:
                 
                username = raw_data['user']['screen_name']
                created_at = str(parser.parse(raw_data['created_at'])).encode("utf-8")
                tweet = raw_data['text'].encode("utf-8")
                retweet = raw_data['retweet_count']
                location = raw_data['user']['location']
                
                tokens = nltk.word_tokenize(tweet) # Splitting the sentence into words
                banned_words = ['music','#music','Music','#Music','MUSIC','#MUSIC']
                BanWordCheck = bool(sum(map(lambda x: x in banned_words, tokens))) #Variable to track if the keyword 'Music' was found in the tweet
                if tweet not in tweetChecklist and BanWordCheck == False:
                        
                    tweetChecklist.append(tweet)
                    connect(created_at, tweet,username,location, retweet)  #insert collected data into MySQL database
                    print("Tweet colleted at: {} ".format(str(created_at)))
                        
                else:
                    print("found a duplicate tweet / A word from banned words was found in the tweet: {}".format(str(tweet)))
                    pass
                
        except AttributeError as e:
            print(e)



if __name__ == '__main__':  
# Twitter authetication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=tracklist) #specifying the keywords we want to search on 