import csv


def save_csv(tuple_list, file_name):
    """writes to csv for each submission block

    Args:
        tuple_list (list): takes a list of tuples from a parsed posts
        or comment with submission info
        file_name (string): name of file we want to write to
    """
    with open("data/" + file_name + ".csv", "a") as file:  # append mode
        csv_content = csv.writer(file)
        csv_content.writerows(tuple_list)
        # print(len(tuple_list), "submissions written to " + file_name + " csv file.")
    # return len(tuple_list)
