from requests import get


def ping_url(url):
    return get(url).ok
