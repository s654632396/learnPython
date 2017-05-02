# coding=utf-8 

import requests
import json
from requests import exceptions

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

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status() # 显示抛出http异常
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else :
        print response.status_code
        print response.reason


if __name__ == '__main__':
    # build_request()
    # build_json()
    timeout_request()