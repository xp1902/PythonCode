encoding = 'utf-8'
from urllib import request
class HtmlDownloader(object):
    def download(self, url):
        req = request.urlopen(url)
        if req.getcode() != 200:
            print('No such file found at %s' % url)
            return None
            return req.read()