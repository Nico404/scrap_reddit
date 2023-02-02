def load_processed_ids(type):
    """
    Reads the processed post ids from the file "data/processed_{type}_ids.txt".
    Returns them as a set

    Args:
        type (str): 'post' or 'comment', used to determine the file name to write to
    Returns:
        set: contains all previous processed submissions from data/processed_{type}_ids.txt
    """
    processed_ids = set()
    filename = f"data/processed_{type}_ids.txt"
    try:
        with open(filename, "r") as f:
            for line in f:
                processed_ids.add(line.strip())
    except FileNotFoundError:
        open(filename, "w").close()
    return processed_ids


def save_processed_ids(submissions, type):
    """
    Takes a list of submissions (posts or comments) as input,
    Opens & Writes in append mode the file "data/processed_{type}_ids.txt"
    So submissions can't be processed twice and generate duplicates.

    Args:
        submissions (List): list of post in json format (type t3)
        type (str): 'post' or 'comment', used to determine the file name to write to
    """
    filename = f"data/processed_{type}_ids.txt"
    with open(filename, "a") as f:
        for submission in submissions:
            f.write(submission["data"]["id"] + "\n")
