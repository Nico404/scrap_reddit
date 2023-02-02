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

    with tqdm(total=None, desc="Fetching Reddit Posts 25 at a time") as pbar:
        while True:
            result, after = get_posts(access_token, subreddit, after)
            time.sleep(0.3)
            if result:
                after = after
                pbar.update(1)
            else:
                "Nothing more to get..."
                break

    with tqdm(total=None, desc="Fetching Reddit comments from fetched posts") as pbar:
        for id in load_processed_ids("post"):
            result = get_comments(access_token, subreddit, id)
            time.sleep(0.3)
            pbar.update(1)


if __name__ == "__main__":
    main()
