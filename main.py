from tqdm import *

from src.save_csv import save_csv
from src.get_submission_API import get_posts, get_comments
from src.parse_submission_API import parse_posts, parse_comments
from private.get_token import get_token


access_token = get_token()
subreddit = "AmItheAsshole"

submission_posts = get_posts(access_token, subreddit)  # first call when after is None
posts, after = parse_posts(submission_posts)

for loop in tqdm(range(50000)):
    posts, after = parse_posts(get_posts(access_token, subreddit, after=after))
    save_csv(posts, "posts_v2_2")
    for post in posts:
        submission_comments = get_comments(access_token, subreddit, post[0])
        comments = parse_comments(submission_comments)
        save_csv(comments, "comments_v2_2")
