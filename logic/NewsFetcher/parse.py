from pathlib import Path

from bs4 import BeautifulSoup

from NewsFetcher.downloader import download_news
from config import *


def news_path(id):
    folder_path = NEWS_FOLDER + str(id) + '/'
    return folder_path + 'news.html'


class NewsParser:

    def _open_news(self):
        path = news_path(self.id)
        if not Path(path).is_file():
            try:
                download_news(self.id)
            except Exception:
                return None
        try:
            file = open(news_path(self.id))
            html = ''.join(file.readlines())
            file.close()
            return html
        except FileExistsError:
            return None

    @staticmethod
    def _clear_str(string):
        return string.strip().replace('\xa0', ' ')


    def get_date(self):
        date_div = self.soup.find('div', {'class': 'date'})
        time = date_div.strong.string
        day = date_div.span.string
        return time.strip() + ' ' + day.strip()

    def get_header(self):
        return self._clear_str(self.soup.find('h1').string)

    def get_text(self):
        news_block = self.soup.find('div', {'class': 'typical'}).span
        news_pars = news_block.find_all('p')
        parsed_pars = []
        for par in news_pars:
            string = par.text
            parsed_pars.append(self._clear_str(string))
        return '\n'.join(parsed_pars)

    def __init__(self, id):
        self.id = id
        self.news_entry = {
            'date': None,
            'header': None,
            'text': None
        }
        self.html = self._open_news()
        if self.html is None:
            self.success = False
        else:
            self.success = True
            self.soup = BeautifulSoup(self.html, 'html.parser')

