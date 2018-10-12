import requests
import json
URL = 'https://www.amazon.cn/dp/B0186FESGW/ref=sd_allcat_kindle_l3_ki'


def json_requests():
    req = requests.get(build_url('user'), auth=('xp1902', 'xp1213800'), json={'name': 'daletina', 'email': '2911577'
                                                                                                             '624@qq.com'})
    print(req.status_code)
    print(req.reason)
    print(better_print(req.text))


def headers_requests():
 ''''更进一步讲，Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去。

注意: 所有的 header 值必须是 string、bytestring 或者 unicode。'''
    headers = {'user-agent': 'Mozilla/5.0'}
    req = requests.get(URL2, headers=headers)
    print(req.status_code)
    print(req.reason)
    print(better_print(req.text))


def build_url(endpoint):
    return '/'.join([URL, endpoint])


def better_print(json_str):
    return json.dump(json.load(json_str), indent=4)


def timeout_requests():
    try:
        response = requests.get(URL, timeout=30)
        response.raise_for_status()
    except:
        print('error')
    else:
        print(response.text)
        print(response.status_code)
if __name__ == '__main__':
    timeout_requests()