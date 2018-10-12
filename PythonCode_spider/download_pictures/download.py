import requests
import os
import re
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
                        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


def download_html(url1, param):
    try:
        r = requests.get(url1, params=param, headers=headers)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ""


def picture_parser(urlst, html):
    urlst1 = re.findall(r'src="https://cdn\.pixabay\.com/photo[0-9a-zA-Z_/-]*\.jpg"', html)
    urlst2 = re.findall(r'data-lazy="https://cdn\.pixabay\.com/photo[0-9a-zA-Z_/-]*\.jpg"', html)
    urlsts = urlst1 + urlst2
    for i in range(len(urlsts)):
        url = eval(urlsts[i].split('=', 1)[1])
        url_improved = url.replace('__340', '_960_720')
        urlst.append(url_improved)


if __name__ == '__main__':
    count = 1
    timer = 0
    urlst = []
    root = 'G://pic//'
    url = 'https://pixabay.com/zh/photos/'
    word = input('please input the key word: ')

    for i in range(5):
        param = {'q': word, 'pagi': count, 'order': 'latest'}
        root_r = root + word + '//'
        html = download_html(url, param)
        picture_parser(urlst, html)

        if not os.path.exists(root_r):
            os.makedirs(root_r)
        for i in range(len(urlst)):
            path = root_r + urlst[i].split('/')[-1]
            if not os.path.exists(path):
                req = requests.get(urlst[i])
                with open(path, 'wb') as f:
                    f.write(req.content)
                print("\r当前进度: {0:.2f}%第{1:1}张".format(timer * 100 / len(urlst), count), end="")
                timer = timer + 1
            else:
                pass
        count = count + 1