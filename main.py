import time
from datetime import datetime, timedelta
from tqdm import tqdm

from src.url_generator import url_generator
from src.get_posts import get_posts
from src.parse_posts import parse_posts
from src.save_csv import save_csv
from src.utc_day import utc_day


start_datetime = datetime(2023, 1, 27, 0, 0)
end_datetime = datetime(2023, 1, 15, 0, 0)

day_list = utc_day(start_datetime, end_datetime)

for day in (progress_bar := tqdm(day_list)):
    progress_bar.set_description(f"processing {day}")

    url = url_generator(day[1], day[2])
    posts = get_posts(url)
    save_csv(parse_posts(posts))  # writes content of API URL to csv file
