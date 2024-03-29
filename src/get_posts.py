import requests
import json
import csv
import time

from src.processed_ids import load_processed_ids
from src.get_post_response import get_post_response
from src.get_new_submissions import get_new_submissions
from src.processed_ids import save_processed_ids
from src.write_to_csv import write_posts_to_csv


def get_posts(access_token, subreddit):
    """
    This function retrieves the top 25 posts from a given subreddit and writes new, unprocessed posts to a CSV file.
    The function uses the given access token to authenticate the request and the Reddit API endpoint.
    If the parameter "after" is stored in file, the function retrieves posts that come after (more recent) that specific post.

    Args:
        access_token (str): The access token used to authenticate the request
        subreddit (str): The subreddit to retrieve posts from

    Returns:
        tuple:full JSON response from the Reddit API
        If no new posts are retrieved, returns None.
    """
    headers = {
        "Authorization": "bearer " + access_token,
        "User-Agent": "Nico404",
    }
    api = "https://oauth.reddit.com"
    params = {"limit": "25", "sort_by": "top"}

    try:
        with open("data/last_after.txt", "r") as f:
            after = f.read()  # set after param with most recent id from last_after.txt
    except FileNotFoundError:
        after = None

    if after:
        params["after"] = after

    processed_post_ids = load_processed_ids("post")
    response = get_post_response(headers, api, subreddit, params)

    if response:
        response_json = response.json()  # full listing type with after and children
        after = response_json["data"]["after"]
        posts = response_json["data"]["children"]  # only t3 type == actual post
        new_posts = get_new_submissions(posts, processed_post_ids)
        if new_posts:
            save_processed_ids(new_posts, "post")
            write_posts_to_csv(new_posts)
            if after:
                with open("data/last_after.txt", "w") as f:
                    f.write(after)
            return response_json
        else:
            print("All posts have been processed.")
            with open("data/last_after.txt", "w") as f:
                f.write("")
            return None
    else:
        return None
