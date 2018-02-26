import requests


ARTICLES_URL = 'https://api.elifesciences.org/articles'


def get_data(url=''):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    return {}


def get_article_items():
    return get_data(url=ARTICLES_URL)['items']


if __name__ == '__main__':
    pass
