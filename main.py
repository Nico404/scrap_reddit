from tqdm import tqdm
import time

from private.get_token import get_token
from src.get_posts import get_posts
from src.get_comments import get_comments
from src.processed_ids import load_processed_ids


def main():
    access_token = get_token()
    subreddit = "AmItheAsshole"
    after = None

    with tqdm(total=None, desc="Fetching Reddit Posts & their comments") as pbar:
        while True:
            posts, after = get_posts(access_token, subreddit, after)
            if posts:
                after = after
                pbar.update(1)
                time.sleep(2)
                for post in posts:
                    get_comments(access_token, subreddit, post[0])
                    time.sleep(2)
            else:
                "Nothing more to get..."
                break


if __name__ == "__main__":
    main()
