import requests
import time


def get_post_response(headers, api, subreddit, params):
    """
    Sends a GET request to a specified Reddit API endpoint with the given headers and parameters.

    Args:
        headers (dict): A dictionary containing the request headers
        api (str): The base URL of the Reddit API endpoint
        subreddit (str): The name of the subreddit to retrieve posts from
        params (dict): A dictionary of query parameters to send with the request

    Returns:
        response (requests.Response or None): The response object from the GET request. If an exception occurs, returns None.
    """
    try:
        response = requests.get(
            "{}/r/{}/".format(api, subreddit),
            headers=headers,
            params=params,
            timeout=5,
        )
    except requests.exceptions.Timeout:
        time.sleep(5)
        response = requests.get(
            "{}/r/{}/".format(api, subreddit),
            headers=headers,
            params=params,
            timeout=5,
        )

    except Exception as e:
        print("Error fetching posts:", e)
        print("API endpoint:", api)
        print("Headers:", headers)
        print("Params:", params)
        return None

    return response
