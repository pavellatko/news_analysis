from bs4 import BeautifulSoup
from config import *
from pathlib import Path
from downloader import download_news


def news_path(id):
    folder_path = NEWS_FOLDER + str(id) + '/'
    return folder_path + 'news.html'


class NewsParser:

    def _open_news(self):
        path = news_path(self.id)
        if not Path(path).is_file():
            download_news(self.id)
        try:
            file = open(news_path(self.id))
            html = ''.join(file.readlines())
            file.close()
            return html
        except FileExistsError:
            return None

    def get_header(self):
        pass

    def __init__(self, id):
        self.id = id
        self._open_news()
        self.news_entry = {
            'date': None,
            'header': None,
            'text': None
        }

