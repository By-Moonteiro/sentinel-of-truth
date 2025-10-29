import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.json_handler import Handler
from src.logic.manager import ManageNews


def test_register_news():
    ManageNews.register_news()

test_register_news()