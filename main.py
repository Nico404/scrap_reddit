from src.url_generator import url_generator
from src.get_posts import get_posts
from src.parse_posts import parse_posts
from src.save_csv import save_csv
import time


pull_nb = int(input('Number of post submissions to pull: '))

for i in range(pull_nb):
    with open(r"data/test.csv", 'r') as file:
        # print('Total lines:', len(file.readlines()))
        try:
            csv_last_utc = file.readlines()[-1].split(',')[2]
            url = url_generator(str(int(csv_last_utc) - 1))  # avoid duplicates identitcal utc
        except IndexError:
            print("empty file, initializing csv_last_utc...")
            csv_last_utc = None
            url = url_generator()

        print(url, csv_last_utc)
        posts = get_posts(url)
        save_csv(parse_posts(posts)) # writes content of API URL to csv file
        time.sleep(0.1)