import requests


class URLReader:

    def parseURL(self, url):
        r = requests.get(url)
        data = r.json()
        return data
