import requests
import json
import time


def get_posts(access_token, subreddit, after=None):
    """Gets a list of posts from an API URL
    given a specific subreddit. It also returns
    an after id to allow for pagination mecanism.

    Args:
        access_token (string): access token generated with secret key from a private get_token function
        subreddit (string): subreddit name: ie "AmItheAsshole"
        after (string, optional): post id of next post to get. Defaults to None.

    Returns:
        json object of Listing containing the post and a bunch of other things
    """
    headers = {
        "Authorization": "bearer " + access_token,
        "User-Agent": "ChangeMeClient/0.1 by TPS_Baboon",
    }
    params = {"limit": "10", "sort_by": "top"}
    if after:
        params["after"] = after

    api = "https://oauth.reddit.com"
    response = requests.get(
        "{}/r/{}/hot/".format(api, subreddit),
        headers=headers,
        params=params,
    )
    data = response.json()
    try:
        return data
    except KeyError:
        print("KeyError: 'data' not found in the json get_post response")
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("RequestsJSONDecodeError")
        time.sleep(1000)
        return None, None


def get_comments(access_token, subreddit, post_id):
    """Gets a list of comments from an API URL
    given a specific subreddit and a particular post id.

    Args:
        access_token (string): access token generated with secret key from a private get_token function
        subreddit (string): subreddit name: ie "AmItheAsshole"
        post_id (string): the id of a specific reddit post

    Returns:
        json object of Listing containing the post and a bunch of other things
    """
    headers = {
        "Authorization": "bearer " + access_token,
        "User-Agent": "ChangeMeClient/0.1 by TPS_Baboon",
    }
    api = "https://oauth.reddit.com"
    response = requests.get(
        "{}/r/{}/comments/{}".format(api, subreddit, post_id),
        headers=headers,
        params={"limit": "100", "sort_by": "top"},
    )
    try:
        return response.json()
    except KeyError:
        print("KeyError: 'data' not found in the json get_post response")
    except (requests.exceptions.ConnectionError, json.decoder.JSONDecodeError):
        print("RequestsJSONDecodeError")
        time.sleep(1000)
        return None
