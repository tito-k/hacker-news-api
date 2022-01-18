import requests
from datetime import datetime

from items.models import Base


def get_latest_published_news():
    latest_news = requests.get(
        'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
    data = latest_news.json()
    top_100_latest_news = data[:100]
    for i in top_100_latest_news:
        get_items = requests.get(
            f'https://hacker-news.firebaseio.com/v0/item/{i}.json?print=pretty')
        response = get_items.json()
        if response:
            if 'id' in response:
                id = response['id']
            if 'type' in response:
                type = response['type']
            if 'by' in response:
                by = response['by']
            else:
                by = None
            if 'time' in response:
                time = datetime.utcfromtimestamp(response['time'])
            else:
                time = None
            if 'kids' in response:
                kids = response['kids']
            else:
                kids = None
            if 'parts' in response:
                parts = response['parts']
            else:
                parts = None
            if 'parent' in response:
                parent = response['parent']
            else:
                parent = None
            if 'text' in response:
                text = response['text']
            else:
                text = None
            if 'descendants' in response:
                descendants = response['descendants']
            else:
                descendants = None
            if 'score' in response:
                score = response['score']
            else:
                score = None
            if 'url' in response:
                url = response['url']
            else:
                url = None
            if 'title' in response:
                title = response['title']
            else:
                title = None
            try:
                Base.objects.get(id=id)
            except Base.DoesNotExist:
                Base.objects.create(id=id, type=type, by=by, time=time, kids=kids, parts=parts,
                                    parent=parent, text=text, descendants=descendants, score=score, url=url, title=title)


def get_top_level_published_news():
    top_news = requests.get(
        'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    data = top_news.json()
    top_100_top_news = data[:100]

get_latest_published_news()


# exec(open('../hacker_news/items/tasks.py').read())