import requests


def check_url_alive(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
        return True
    except requests.exceptions.HTTPError:
        return False
