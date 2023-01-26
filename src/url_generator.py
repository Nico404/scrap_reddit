import requests


def url_generator(before = 1674514800):
    """This function returns the url for the API URL page
       of the broken pushshift API, generated from the unofficial
       mirror https://camas.unddit.com/

    Returns:
        string:
        https://api.pushshift.io/reddit/submission/search?html_decode=true&after=0&before=1674514800&subreddit=AmItheAsshole&size=10
    """

    base = 'https://api.pushshift.io/reddit/submission/search'

    parameters = {
        'html_decode': 'true',
        'after': 0,
        'before': before,
        'subreddit': 'AmItheAsshole',
        'size': 10  # number of posts requested
    }

    response = requests.get(base, params=parameters)
    return response.url
