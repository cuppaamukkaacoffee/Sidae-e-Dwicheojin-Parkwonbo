import urllib.request
import io


def get_robots_txt(url):
    try:
        req = urllib.request.urlopen(url + 'robots.txt', data=None)
    except:
        return ""
    data = io.TextIOWrapper(req, encoding='utf-8')
    return data.read()

