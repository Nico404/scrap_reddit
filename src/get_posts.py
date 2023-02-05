import requests
import json
import csv
import time

from src.processed_ids import load_processed_ids
from src.get_post_response import get_post_response
from src.get_new_submissions import get_new_submissions
from src.processed_ids import save_processed_ids
from src.write_to_csv import write_posts_to_csv


def get_posts(access_token, subreddit, after=None, before=None):
    """
    This function retrieves the top 25 posts from a given subreddit and writes new, unprocessed posts to a CSV file.
    The function uses the given access token to authenticate the request and the Reddit API endpoint.
    If the parameter "after" is provided, the function retrieves posts that come after that specific post.

    Args:
        access_token (str): The access token used to authenticate the request
        subreddit (str): The subreddit to retrieve posts from
        after (str, optional): The identifier of a specific post to retrieve posts after. Defaults to None.

    Returns:
        tuple: A tuple containing two elements, full JSON response from the Reddit API and identifier of the last post in the response.
        If no new posts are retrieved, returns (None, None).
    """

    # Load the last after value from file
    try:
        with open("data/last_after.txt", "r") as f:
            after = f.read()
    except FileNotFoundError:
        after = None

    try:
        with open("data/last_before.txt", "r") as f:
            before = f.read()
    except FileNotFoundError:
        before = None

    headers = {
        "Authorization": "bearer " + access_token,
        "User-Agent": "Nico404",
    }
    api = "https://oauth.reddit.com"
    params = {"limit": "25", "sort_by": "top"}

    if after:
        params["after"] = after
        params["before"] = None

    if before:
        params["before"] = before
        params["after"] = None

    processed_post_ids = load_processed_ids("post")
    response = get_post_response(headers, api, subreddit, params)

    if response:
        response_json = response.json()  # full listing with after and children
        after = response_json["data"]["after"]
        if after:
            with open("data/last_after.txt", "w") as f:
                f.write(after)

        posts = response_json["data"]["children"]  # only t3 type == actual post
        new_posts = get_new_submissions(posts, processed_post_ids)
        if new_posts:
            save_processed_ids(new_posts, "post")
            write_posts_to_csv(new_posts)
            return response_json, after
        else:
            print("All posts have been processed. Moving backwards...")
            with open("data/last_after.txt", "w") as f:
                f.write("")  # empty after
            if before:
                with open("data/last_before.txt", "w") as f:
                    f.write(before)  # set before
            print(response_json, before)
            return response_json, before
    else:
        return None, None
