def get_new_submissions(submissions, processed_ids):
    """mechanism to check if submission post or comment was already processed

    Args:
        submissions (dict): reddit posts or comments
        processed_ids (set): set of already processed ids for post or comment

    Returns:
        new_submissions (dict): filtered submissions
    """
    new_submissions = []
    for submission in submissions:
        if (
            submission["data"]["id"] not in processed_ids
            and submission["kind"] != "more"
            and submission["data"]["stickied"] == False
        ):
            new_submissions.append(submission)
    return new_submissions
