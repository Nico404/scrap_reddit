from src.url_generator import url_generator
from src.get_posts import get_posts
from src.parse_posts import parse_posts
from src.save_csv import save_csv


url = url_generator()
posts = get_posts(url)
save_csv(parse_posts(posts)) # writes content of API URL to csv file

with open(r"data/test.csv", 'r') as file:
    # print('Total lines:', len(file.readlines()))
    csv_last_utc = file.readlines()[-1].split(',')[4]
