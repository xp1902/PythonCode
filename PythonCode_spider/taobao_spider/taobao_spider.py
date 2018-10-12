import re
import requests
from bs4 import BeautifulSoup


def download_page(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return " "


def parser_html(ilist, html):
    # soup = BeautifulSoup(html, 'html.parser')
    # plist = soup.find_all('span', {'class': 'price g_price g_price_highlight'})
    # nlist = soup.find_all('a', {'class': 'product_title'})
    plis = re.findall(r'"price"\:\"[\d\.]*\"', html)
    nlis = re.findall(r'"title"\:\".*?\"', html)
    for i in range(len(plis)):
        plist = eval(plis[i].split(':')[1])
        nlist = eval(nlis[i].split(':')[1])
        ilist.append([plist, nlist])


def printer_info(ilist):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品", chr(12288)))
    count = 0
    for g in ilist:
        count = count + 1
        print(tplt.format(count, g[0], g[1], chr(12288)))


if __name__ == '__main__':
    goods = '鼠标'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(48 * i)
            html = download_page(url)
            parser_html(infolist, html)
        except:
            continue
    printer_info(infolist)



