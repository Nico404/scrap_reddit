# scrap_reddit
little python project for scrapping AITA subreddit.
The goal is to get post submissions and their best comments to train 
an AI model to answer an AITA prompt

Since pushshift api wrappers PAWR and PSAW are down or not maintened at the moment, and the first attempt to use pushshift API yielded unexpected results from comments & overall unreliable data... 

This little project is based on generated API URL from the Reddit Official API 
https://www.reddit.com/dev/api/


# Data Science

Fetch tons of reddit submission posts & associated comments.
There needs to be enough comments on the posts.

## 2 goals

1. be able to give a verdict: YTA => **classification problem**

- naive approach => count number of NTA, YTA, ESH, NTA... => show distribution

- Zero-Shot Classification
Text Input: post title / post content
Candidate Labels: YTA, YWBTA, NTA, YWNBTA, ESH, NAH, INFO
Output: YTA 0.900 NTA 0.100 ESH 0.000...

- LLM to "fine-tuner" ?


2. be able to generate an answer based on context: YTA, that's why... => **text generation problem**

- find a model and feed him the submission post (and verdict from 1?). 
=> verdict + text generated
- conversational ??, Question answering with only context and no question ??