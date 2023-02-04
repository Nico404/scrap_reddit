import csv


def write_posts_to_csv(posts):
    """
    Writes a post submission to a csv file

    Args:
        posts (dict): content of a reddit post
    """
    with open("data/posts_v4.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "num_comments", "body", "title", "url"]
        )
        for post in posts:
            if post["data"]["stickied"] == False:  # Get rid of posts from mods & such
                writer.writerow(
                    {
                        "id": post["data"]["id"],
                        "num_comments": post["data"]["num_comments"],
                        "body": post["data"]["selftext"].replace(
                            "\n", ""
                        ),  # avoid LR in file
                        "title": post["data"]["title"],
                        "url": post["data"]["url"],
                    }
                )


def write_comments_to_csv(comments):
    """
    Writes a comment submission to a csv file

    Args:
        comments (dict): content of a reddit comment
    """
    with open("data/comments_v4.csv", "a", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "parent_id", "score", "body", "permalink"]
        )
        for comment in comments:
            try:
                if (
                    comment["data"]["stickied"] == False and comment["kind"] != "more"
                ):  # no sub topics
                    writer.writerow(
                        {
                            "id": comment["data"]["id"],
                            "parent_id": comment["data"]["parent_id"],
                            "score": comment["data"]["score"],
                            "body": " ".join(comment["data"]["body"].splitlines()),
                            "permalink": comment["data"]["permalink"],
                        }
                    )
            except Exception as e:
                print(comment)
