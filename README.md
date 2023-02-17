# scrap_reddit
This little python project for scrapping the /r/AITA subreddit.
The goal is to get post submissions and their best comments to train an AI model to answer an AITA prompt

Since the Pushshift API wrappers PAWR and PSAW are down or not maintained at the moment, and the first attempt to use the Pushshift API yielded unexpected results from comments & overall unreliable data we have based it on the Reddit Official API. It uses a simple pagination mechanism & saves already-processed posts persistently.

https://www.reddit.com/dev/api/

The content that can be pulled from the API at any given time is very limited by Design, so it is required to run this a few times to get a big enough Dataset. 


[posts data sample](data/posts_v4_sample.csv) </br>
[comments data sample](data/comments_v4_sample.csv) </br>
