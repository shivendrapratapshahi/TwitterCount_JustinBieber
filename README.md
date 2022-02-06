# Data Pipeline for TwitterCount_JustinBieber

#Steps for the Solution

*Created a Twitter account and API credentials

*Downloade any opensource Database - Decided to download MySQL database because of it's widespread use

*Install the Tweepy and mysql-connector Python Libraries

*After looking at the twitter documentation, I found the most important and useful fields to extract for our dataset from the twitter API: username, created_at, tweet, retweet_count and location of the tweet.

*I created an object for my class 'StdOutListener' and extracted all the tweets from the API with the filter '#justinbieber' in it.

*Before storing it in my database, I implemented a few checks:

*Kept a track of Number of tweets: tweetCount

*Filtering out duplicate tweet by initialising a list and checking if the tweet has already been consumed.

*Since the previous step has been executed, Number of tweets and Number of unique tweets will remain same.

*I'm also filtering out on the keyword '#music' or 'music'.

*Final step is to store the tweet and it's related information in the database.


# Questions

* What are the risks involved in building such a pipeline?
Ans: Data Security, Data Senstivity, Increase in volume of Data. Data masking is required if there is sensitive information. Access to API keys.

*How would you roll out the pipeline going from proof-of-concept to a production ready solution?
Ans: Typically, you roll out to a production environment in stages. A staged rollout is especially important for large deployments that affect a significant number of users.
The staged deployment can start with a small set of users and eventually expand the user base until the deployment is available to all users. A staged deployment can also start with a limited set of services and eventually phase in the remaining services. Staging services in phases can help isolate, identify, and resolve problems a service might encounter in a production environment.

*What would a production ready solution entail that a POC wouldn't?
Ans: Auto Scaling -- when the tweets for the given filter increase in volume, the pipeline should scale automatically.  

*What is the level of effort required to deliver each phase of the solution?

*What is your estimated timeline for a production ready solution?
