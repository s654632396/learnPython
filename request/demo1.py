# coding=utf-8 

import requests
import json

base_url = 'https://api.github.com'

def build_uri(end_point):
    return '/'.join([base_url, end_point])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def build_request():
    response = requests.get(build_uri('users/emails'), auth=('imoocdemo','imoocdemo123'))
    print better_print(response.text)
    # print response.text

if __name__ == '__main__':
    build_request()