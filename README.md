# scrap_reddit
This little python project for scrapping the /r/AITA subreddit.
The goal is to get post submissions and their best comments to train an AI model to answer an AITA prompt

Since the Pushshift API wrappers PAWR and PSAW are down or not maintained at the moment, and the first attempt to use the Pushshift API yielded unexpected results from comments & overall unreliable data we have based it on the Reddit Official API. It uses a simple pagination mechanism & saves already-processed posts persistently.

https://www.reddit.com/dev/api/

The content that can be pulled from the API at any given time is very limited by Design, so it is required to run this a few times to get a big enough Dataset. 


[posts data sample](data/posts_v4_sample.csv) </br>

<table>
  <tr>
    <th>id</th>
    <th>num_comments</th>
    <th>body</th>
    <th>title</th>
    <th>url</th>
  </tr>
  <tr>
    <td>10uxee0</td>
    <td>1181</td>
    <td>I know this post sounds super petty, but this is the most ridiculous fight I've had with my boyfriend... I was serious though: I'll shave whenever he shaves too.We're at an impasse but I wonder if I am being a little too petty about the whole thing. </td>
    <td>AITA for telling my boyfriend I'll shave my legs if he shaves his?</td>
    <td>https://www.reddit.com/r/AmItheAsshole/comments/10uxee0/aita_for_telling_my_boyfriend_ill_shave_my_legs/</td>
  </tr>
  <td>10ur722</td>
  <td>1849</td>
  <td>My daughter Bryn F9 is going on a trip to a nearby water park with her class next week... She sent me back an email with a bunch of bs that basically ended with “if Bryn goes on the trip, she has to be Ben’s buddy.”</td>
  <td>AITA for not letting my daughter go on a school trip?</td>
  <td>https://www.reddit.com/r/AmItheAsshole/comments/10ur722/aita_for_not_letting_my_daughter_go_on_a_school/</td>
</tr>
</table>

</br>

[comments data sample](data/comments_v4_sample.csv) </br>

<table>
  <tr>
    <th>comment_id</th>
    <th>parent_id</th>
    <th>score</th>
    <th>body</th>
    <th>permalink</th>
  </tr>
  <tr>
    <td>j7dy9fw</td>
    <td>t3_10qxvu1</td>
    <td>7</td>
    <td>The post about the bratty daughter and the seafood restaurant is rife with commenters creating mental disorders for the daughter to scrub accountability for her behaviour. Honestly kinda dangerous</td>
    <td>/r/AmItheAsshole/comments/10qxvu1/aita_monthly_open_forum_february_2023_trolls/j7dy9fw/</td>
  </tr>
  <tr>
    <td>j7ctunm</td>
    <td>t3_10qxvu1</td>
    <td>7</td>
    <td>My subconscious chose the wrong option for a report I feel so embarrassed even though I don’t think it’s a big deal 🥲  Just wanted to say that somewhere</td>
    <td>/r/AmItheAsshole/comments/10qxvu1/aita_monthly_open_forum_february_2023_trolls/j7ctunm/</td>
  </tr>
</table>
