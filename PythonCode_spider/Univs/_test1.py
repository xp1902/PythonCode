import requests
from bs4 import BeautifulSoup
import bs4


def html_download(URL):
    try:
        req = requests.get(URL, timeout=30)
        req.encoding = 'utf-8'
        req.raise_for_status()
        return r.text
    except:
        print('download error')


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = []
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            data.append([tds[0].string, tds[1].string, tds[3].string])
            return data
    return data


def html_printer(data):
    fout = open('output.html', 'w')
    fout.write('<html>')
    fout.write('<body>')
    fout.write('<table>')
    for d in data:
        fout.write('<tr>')
        fout.write('<td>%s</td>' % data['url'])
        fout.write('<td>%s</td>' % data['title'].encode['utf-8'])
        fout.write('<td>%s</td>' % data['summary'])
        fout.wirte('</tr>')
    fout.write('</table>')
    fout.write('</body>')
    fout.write('</html>')


def main():
    URL = 'http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2017.html'
    html = html_download(URL)
    datas = html_parser(html)
    html_printer(datas)
main()
