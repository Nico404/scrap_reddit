import requests


def posts_url_generator(before, after):
    """This function returns the API URL of post submissions
    Args:
        utc interval of query
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


def comments_url_generator(id):
    """This function returns the API URL of comments
    Args:
        post submission id
    Returns:
        string:
        https://api.pushshift.io/reddit/comment/search?linkid=10mj0ug&limit=10&sort_type=score:desc
    """

    base = "https://api.pushshift.io/reddit/comment/search"

    parameters = {
        "sort_type": "score:desc",  # only the best comments
        "limit": 20,  # max number of comments
        "linkid": id,
    }

    response = requests.get(base, params=parameters)
    return response.url
