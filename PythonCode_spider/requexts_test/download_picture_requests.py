#!/usr/bin/env python3
import requests
from PIL import Image
from io import BytesIO
import os
url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2338643698,4051309964&fm=23&gp=0.jpg'
root = 'G://pics//'
path = root + url.split('/')[-1]
'''try:
    if not os.path.exists(root):
        os.makedirs(root)

    if not os.path.exists(path):
        req = requests.get(url)
        with open(path, 'wb') as f:
            f.write(req.content)
            f.close()
        print("Download over.")
    else:
        print('file has been created')
except:
    print('download error')'''
req = requests.get(url)
i = Image.open(BytesIO(req.content))
print(i)