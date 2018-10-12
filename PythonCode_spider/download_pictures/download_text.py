import requests
import re

url = 'https://pixabay.com/zh/photos/?q=天&pagi=1&order=latest'

if __name__ == '__main__':
    r = requests.get(url, timeout=30)
    r.encoding = r.apparent_encoding
    html = r.text
    img1 = re.findall(r'src="https://cdn\.pixabay\.com/photo[0-9a-zA-Z_/-]*\.jpg"', html)
    img2 = re.findall(r'data-lazy="https://cdn\.pixabay\.com/photo[0-9a-zA-Z_/-]*\.jpg"', html)
    img = img1 + img2
    imgs =[]
    for i in range(len(img)):
        imgs.append(img[i].replace('__340', '_960_720'))
        print(eval(imgs[i].split('=', 1)[1]))
    print(len(img))