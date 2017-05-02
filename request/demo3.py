# coding=utf-8 

import requests
import json

base_url = 'https://api.github.com'

def build_uri(end_point):
    return '/'.join([base_url, end_point])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def build_request():
    response = requests.get(build_uri('users'), params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url

def build_json():
    # response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'),
    #                         json={'name':'babyimooc2', 'email':'helloworld@imooc.org'})
    response = requests.post(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),
                             json=['testimoocdemo@mooc.com'])

    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code

def hard_requests():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'fake1.2.3'}
    req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'),headers=headers)
    prereq = req.prepare()
    print prereq.headers
    print prereq.body

    response = s.send(prereq, timeout=5)
    print response.status_code
    print response.request.headers
    print response.text

if __name__ == '__main__':
    # build_request()
    hard_requests()