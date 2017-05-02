# coding=utf-8 
import urllib2, cookielib

url = 'http://www.baidu.com/'

print 'method A:'
response = urllib2.urlopen(url)
print "status code:" , response.getcode()
print "content-length:", len(response.read())

print 'method B:'
request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0')
response = urllib2.urlopen(url)
print "status code:" , response.getcode()
print "content-length:", len(response.read())

print 'method C:'
import cookielib
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print "status code:" , response.getcode()
print "content-length:", len(response.read())
print cj
