import csv


def save_csv(tuple_list):
    """writes a csv line for each post submission

    Args:
        tuple_list (list): takes a list of tuples from parse_posts.py
        with post submission info
    """
    with open('data/test.csv', 'a') as file:  # append mode
        csv_content = csv.writer(file)
        # csv_content.writerow(['title', 'num_comments', 'created_utc', 'url', 'id', 'selftext'])
        csv_content.writerows(tuple_list)
        print(len(tuple_list), 'post submissions written to csv file.')
    return len(tuple_list)