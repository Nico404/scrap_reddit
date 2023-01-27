import requests


def url_generator(before, after):
    """This function returns the url for the API URL page
       of the broken pushshift API, generated from the unofficial
       mirror https://camas.unddit.com/

    Returns:
        string:
        https://api.pushshift.io/reddit/search/submission?subreddit=AmItheAsshole&size=1000&num_comments%3E=10&after=1674691200&before=1674777599&sort_type=num_comments
    """

    base = "https://api.pushshift.io/reddit/submission/search"

    parameters = {
        "after": after,
        "before": before,
        "subreddit": "AmItheAsshole",
        "size": 500,  # number of posts requested
        "sort_type": "num_comments",
        "num_comments": 20,
    }

    response = requests.get(base, params=parameters)
    return response.url
