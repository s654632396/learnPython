# coding=utf-8 

import urllib
import urllib2
url_ip = 'http://localhost:8000/ip'
url_get = 'http://localhost:8000/get'


def use_simple_urllib2():
    response = urllib2.urlopen(url_ip)
    print 'response headers:' \
          '-----------------'
    print response.info()
    print 'response body:' \
          '-----------------'
    print ''.join([line for line in response.readlines()])

def use_params_urllib2():
    params = urllib.urlencode({'param1':'hello', 'param2': 'world'})
    print 'params :' \
          '---------------'
    print params
    response = urllib2.urlopen('?'.join([url_get, '%s']) % params)
    print 'response headers:' \
          '-----------------'
    print response.info()
    print 'response status code:' \
          '------------------'
    print response.getcode()
    print 'response body:' \
          '-----------------'
    print ''.join([line for line in response.readlines()])



if __name__ == '__main__' :
    print '>>> use_simple_urllib2() :'
    use_simple_urllib2()

    print '>>> use_simple_urllib2() :'
    use_params_urllib2()


















