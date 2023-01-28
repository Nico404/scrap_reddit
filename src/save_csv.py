import csv


def save_csv(tuple_list, file_name):
    """writes a csv line for each submission

    Args:
        tuple_list (list): takes a list of tuples from parse_posts or parse_comments
        with submission info
    """
    with open("data/" + file_name + ".csv", "a") as file:  # append mode
        csv_content = csv.writer(file)
        # csv_content.writerow(['title', 'num_comments', 'created_utc', 'url', 'id', 'selftext'])
        csv_content.writerows(tuple_list)
        print(len(tuple_list), "submissions written to " + file_name + " csv file.")
    return len(tuple_list)
