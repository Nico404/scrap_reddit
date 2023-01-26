import unittest
from src.get_posts import get_posts
from src.url_generator import url_generator
from src.parse_posts import parse_posts
from src.save_csv import save_csv


class TestClass(unittest.TestCase):
    def test_url_generator(self):
        url_generator()

    def test_get_posts(url):
        get_posts(url_generator())

    def test_parse_posts(posts):
        parse_posts(get_posts(url_generator()))

    def test_save_csv(tuple_list):
        save_csv(parse_posts(get_posts(url_generator())))

if __name__ == '__main__':
    unittest.main()
