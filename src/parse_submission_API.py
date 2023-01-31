def parse_posts(posts):
    """Parse the fetched Json Post Object and
    extract some interesting data

    Args:
        json object of Listing containing the post and a bunch of other things
        output of get_submission_API get_posts()

    Returns:
        list of tuples with the info we need
        the id of the next post we want to get
    """
    rowList = list()
    after = posts["data"]["after"]
    posts = posts["data"]["children"]
    for post in posts:
        try:
            if post["data"]["stickied"] == False:  # get rid of sub posts from mods
                body = post["data"]["selftext"].replace("\n", "")
                title = post["data"]["title"]
                num_comments = post["data"]["num_comments"]
                url = post["data"]["url"]
                id = post["data"]["id"]

                row = (id, title, num_comments, body, url)
                rowList.append(row)
        except:
            pass

    return rowList, after


def parse_comments(comments):
    """Parse the fetched Json Comment Object and
    extract some interesting data

    Args:
        json object of Listing containing the post and a bunch of other things
        ouput of get_submission_API get_comments()

    Returns:
        list of tuples with the info we need
    """
    rowList = list()
    comments = comments[1]["data"]["children"]  # idx 0 is the actual post
    for comment in comments:
        try:
            if comment["data"]["stickied"] == False:  # no sub topics
                id = comment["data"]["id"]
                parent_id = comment["data"]["parent_id"]
                score = comment["data"]["score"]
                body = " ".join(comment["data"]["body"].splitlines())
                permalink = comment["data"]["permalink"]

                row = (parent_id, id, score, body, permalink)
                rowList.append(row)
        except KeyError:
            pass
    return rowList
