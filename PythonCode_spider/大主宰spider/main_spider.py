import requests
import re
url = 'http://www.xxbiquge.com/0_142/'


def html_download(url):
    try:
        r = requests.get(url)
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return ""


def find_surl(html):
    surls = re.findall(r'<p>最新章节：<a href="[0-9_/]+\.html"', html)
    surl = surls[0].split("/", )[-1].split("\"")[0]
    return url + surl


def main():
    html = html_download(url)
    u = find_surl(html)
    print(u)
    html0 = html_download(u)
    content = re.findall(r'<div id="content">.*?</div>', html0)
    with open('dazhuzai.html', 'w', encoding='utf-8') as fp:
        fp.write("<html>")
        fp.write("<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />")
        fp.write(content[0])

main()



