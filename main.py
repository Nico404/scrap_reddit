import time
from datetime import datetime, timedelta
from tqdm import tqdm

from src.url_generator import posts_url_generator, comments_url_generator
from src.get_submission import get_submission
from src.parse_submission import parse_posts, parse_comments
from src.save_csv import save_csv
from src.utc_day import utc_day


start_datetime = datetime(2023, 1, 27, 0, 0)
end_datetime = datetime(2017, 1, 1, 0, 0)

day_list = utc_day(start_datetime, end_datetime)

for day in (progress_bar := tqdm(day_list)):
    progress_bar.set_description(f"processing {day}")

    url = posts_url_generator(day[1], day[2])
    try:
        posts = get_submission(url)
    except:
        print("error getting submission post")
    save_csv(parse_posts(posts), "posts")  # writes content of API URL to csv file

    for post in posts:
        url = comments_url_generator(post["id"])
        try:
            comments = get_submission(url)
        except:
            print("error getting submission comment")
        save_csv(parse_comments(comments), "comments")
