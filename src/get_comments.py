import requests
import json
import csv
import time

from src.processed_ids import load_processed_ids, save_processed_ids
from src.get_comment_response import get_comment_response
from src.get_new_submissions import get_new_submissions
from src.write_to_csv import write_comments_to_csv


def get_comments(access_token, subreddit, post_id):
    """
    This function retrieves the top 200 comment from a given post and writes new, unprocessed comments to a CSV file.
    The function uses the given access token to authenticate the request and the Reddit API endpoint.

    Args:
        access_token (str): The access token used to authenticate the request
        subreddit (str): The subreddit to retrieve posts from
        post_id (str): The identifier of a specific post. Defaults to None.

    Returns:
        tuple: full JSON response from the Reddit API
        If no new comments are retrieved, returns None
    """

    headers = {
        "Authorization": "bearer " + access_token,
        "User-Agent": "Nico404",
    }
    api = "https://oauth.reddit.com"
    params = {"limit": "200", "sort_by": "top"}

    processed_ids = load_processed_ids("comment")
    response = get_comment_response(headers, subreddit, api, params, post_id)

    if response:
        response_json = response.json()  # full listing
        comments = response_json[1]["data"]["children"]  # actual comment, idx0 is post
        new_comments = get_new_submissions(comments, processed_ids)

        if new_comments:
            save_processed_ids(new_comments, "comment")
            write_comments_to_csv(new_comments)
            return response_json
        else:
            print("All comments have been processed.")
            return None
    else:
        return None
