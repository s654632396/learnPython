# coding=utf-8 

import requests

base_url = 'https://api.github.com'

def construct_url(endpoint):
    return '/'.join([base_url, '%s']) % endpoint

def auth_request():
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo'))

def basic_oauth():
    headers = {'Authorization': ''}
    response = requests.get(construct_url('user'), headers=headers)
    # @todo