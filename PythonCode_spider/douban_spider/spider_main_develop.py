#!/usr/bin/env python
import requests
import codecs
from bs4 import BeautifulSoup
encoding = 'utf-8'
URL_douban = 'http://movie.douban.com/top250'


def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers=headers).text
    return data


def parser_html(html, movie_name_list):
    soup = BeautifulSoup(html, 'html.parser')
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    for movie_li in movie_list_soup.find_all('li'):
        detial = movie_li.find('div', attrs={'class': 'hd'})
        movie_name = detial.find('span', attrs={'class': 'title'}).getText()
        movie_name_list.append(movie_name)
    next_page = soup.find('span', attrs={'class': 'next'})
    if next_page:
        return movie_name_list, URL_douban + next_page.a['href']
    return movie_name_list, None


def main():
    url = URL_douban
    list = []
    with codecs.open('movies1', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parser_html(html, list)
        for i in range(len(movies)):
            fp.write(u'{:}\n'.format(movies[i]))
if __name__ == '__main__':
    main()