def parse_posts(posts):
    """grabs the posts from get_posts.py and turns each post into a tuple

    Args:
        posts (list): list of reddit post submissions

    Returns:
        list of tuples. Each tuple contains a post submission's content
    """
    rowList = list()
    for post in posts:
        if post["selftext"] != "[removed]":  # trash empty posts
            title = post["title"]
            num_comments = post["num_comments"]
            url = post["url"]
            id = post["id"]
            created_utc = post["created_utc"]
            selftext = " ".join(post["selftext"].splitlines())
            row = (id, url, created_utc, num_comments, title, selftext)
            rowList.append(row)
    return rowList
