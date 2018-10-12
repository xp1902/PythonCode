import requests
import re


url = 'http://www.xxbiquge.com/0_142/'

r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
surls = re.findall(r'<p>最新章节：<a href="[0-9_/]+\.html"', html)
surl = surls[0].split("/")[-1].split('\"')[0]
Url = url + surl
'''htlm = requests.get(Url)
html = re.findall(r'<div id="content">.*?</div>', htlm)'''
print(Url)

