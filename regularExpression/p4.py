# coding=utf-8 
import re
import urllib2

req = urllib2.urlopen('https://zh.moegirl.org/%E8%88%B0%E9%98%9FCollection:%E8%A1%A3%E9%98%BF%E5%8D%8E')

buf = req.read()
# print buf

pattern = re.compile(r'<table class="wikitable.+?>[\s\S]+?</table>', re.I)
tabledata = pattern.findall(buf)
# print tabledata
# print len(tabledata)

pattern_td = re.compile(
    r'<tr>[\s\S]+?<td>.*?<span lang="ja">([\s\S]+?)<[\S\s]*?</span>[\s\S]*?<br[ /]*?>([\s\S]+?)</td>[\s\S]+?</tr>', re.I)

voicedata = tabledata[2]

items = pattern_td.findall(voicedata)
for item in items :
    print item[0].decode('utf-8')
    print item[1].decode('utf-8')
