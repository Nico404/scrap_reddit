import time

from private.get_token import get_token
from src.get_posts import get_posts
from src.get_comments import get_comments
from src.processed_ids import load_processed_ids


def main():
    access_token = get_token()
    subreddit = "AmItheAsshole"
    after = None

    while True:
        posts, after = get_posts(access_token, subreddit, after)
        if posts:
            after = after
            time.sleep(1)
            for post in posts["data"]["children"]:
                get_comments(access_token, subreddit, post["data"]["id"])
                time.sleep(1)
        else:
            break


if __name__ == "__main__":
    main()
