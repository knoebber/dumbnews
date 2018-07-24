import feedparser
from os import listdir

def get_feeds(path):
    with open(path) as f:
        links = f.readlines()

    f.close()

    feeds = []

    for feed in links:
        feeds.append(feedparser.parse(feed))

    return feeds

def list_titles():
    return listdir('dumbnews/feeds')

def get_path(title):
    return 'dumbnews/feeds/{}'.format(title)
