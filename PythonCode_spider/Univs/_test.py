import requests
from bs4 import BeautifulSoup


def html_download(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def html_parser(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    tods = soup.tbody
    for r in tods.find_all('tr'):
        tds = r('td')
        ulist.append([tds[0].string, tds[1].string, tds[3].string])

if __name__ == '__main__':
    Ulist = []
    num = input('number: ')
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = html_download(url)
    html_parser(html, ulist)
    for i in range(int(num)):
        u = Ulist[i]
        print('{0:^10}\t{1:{3}^10}\t{2:^10}'.format(u[0], u[1], u[2], chr(12288)))
