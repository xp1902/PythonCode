import requests
import re
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return" "


def fill_list(list, url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    h = soup.find_all('a')
    for i in h:
        try:
            href = i.attrs['href']
            list.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue


def print_list(list, url, opfile):
    for stock in list:
        stock_infohtml = url + stock + ".html"
        html = get_html(stock_infohtml)
        try:
            if html == "":
                continue
            infodict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockinfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockinfo.find_all(attrs={'class': 'bets-name'})[0]
            infodict.update({"股票名称": name.text.split()[0]})

            keylist = stockinfo.find_all('dt')
            valuelist = stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key  = keylist[i].text
                val = valuelist[i].text
                infodict[key] = val
            with open(opfile, 'a', encoding='utf-8') as f:
                f.write(str(infodict) + '\n')
        except:
            continue

if __name__ == '__main__':
    stockUrl = "http://quote.eastmoney.com/stocklist.html"
    stockInfo = "https://gupiao.baidu.com/stock/"
    output = "D://gupiao.txt"
    stock_list = []
    fill_list(stock_list, stockUrl)
    print_list(stock_list, stockInfo, output)