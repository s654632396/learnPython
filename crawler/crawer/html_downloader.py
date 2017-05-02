# coding=utf-8

import re
import urllib2

class Downloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            raise Exception, 'Sorry, Craw failed!'
        else :
            return response.read()


