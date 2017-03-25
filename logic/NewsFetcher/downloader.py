import urllib
from os import mkdir
from urllib.request import urlopen
from config import *


def download_page(url, save_path):
    html = urlopen(url).read().decode('utf-8')
    file = open(save_path, 'w')
    print(html,file=file)
    file.close()


def download_news(id):
    folder_path = NEWS_FOLDER + str(id) + '/'
    try:
        mkdir(folder_path)
    except FileExistsError:
        pass
    print(folder_path + 'news.html')
    print(folder_path + 'comments.html')
    download_page(NESW_MASK % id, folder_path + 'news.html')
    download_page(COMMENTS_MASK % id, folder_path + 'comments.html')
