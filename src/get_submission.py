import requests
import json


def get_submission(url):
    """retrieves a list of reddit post submissions from url

    Args:
        url (string): takes an API URL pushshift like output of url_generator
    Returns:
        list: list of reddit post submissions
    """
    response = requests.get(url)
    jsonDict = response.json()
    posts = jsonDict["data"]
    return posts
