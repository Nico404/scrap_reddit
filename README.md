# scrap_reddit
little python project for scrapping AITA subreddit.
The goal is to get post submissions and their best comments in order to train an AI model to answer an AITA prompt

Since pushshift api wrappers PAWR and PSAW are down or not maintened at the moment, and the first attempt to use pushshift API yielded unexpected results from comments & overall unreliable data... 

This little project is based on the Reddit Official API, and uses simple pagination parameter usage.
https://www.reddit.com/dev/api/

Since the Content that can be pull from the API at any given time is very limited, it is required to run this a few time to get a big enough Dataset. 
