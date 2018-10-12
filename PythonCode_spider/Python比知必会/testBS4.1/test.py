#!/usr/bin/evn python
'''
created on 2017.7.08
@author: tlion\
'''


import requests
from bs4 import BeautifulSoup


class Item(object):
    title = None
    firstAuthor = None
    firstName = None
    reNum = None
    content = None
    lastAuthor = None
    lastTime = None


class GetInfo(object):
    def __int__(self, url):
        self.url = url
        self.pageSum = 5
        self.url = self.get_urls(self.pageSum)
        self.item = self.spider(self.url)
        self.pipelines(self.item)

    def get_urls(self, pageSum):
        urls = []
        return urls

    def spider(self, url):
        items = []
        return items

    def pipelines(self, items):
        pass

    def getResponseContent(self, url):
        pass

if __name__ == '__main__':
    url = u'http://tieba.baidu.com/f?kw=权利的游戏&ie=utf-8&pn=50'
    GTI = GetInfo(url)
