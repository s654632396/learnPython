# coding=utf-8 
import requests

url_ip = 'http://localhost:8000/ip'
url_get = 'http://localhost:8000/get'


def use_simple_requests():
    response = requests.get(url_ip)
    print 'response headers:' \
          '-----------------'
    print response.headers
    print 'response body:' \
          '-----------------'
    print response.text

def use_params_requests():
    response = requests.get(url_get, {'param1':'hello', 'param2': 'world'})
    print 'response headers:' \
          '-----------------'
    print response.headers
    print 'response status code:' \
          '------------------'
    print response.status_code
    print response.reason
    print 'response body:' \
          '-----------------'
    print response.json()



if __name__ == '__main__' :
    print '>>> use_simple_requests() :'
    use_simple_requests()

    print '>>> use_simple_requests() :'
    use_params_requests()


