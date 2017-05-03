# coding=utf-8

"""
DOM vs SAX
操作XML 有2种方法
DOM会读入整个XML到内存，解析为TREE，因此内存占用高，解析慢
SAX是流模式，边读边解析，内存占用小，解析快，但是需要额外处理事件
"""
"""
SAX 解析器读到一个node：
    <a href="/example/python">python</a>
会产生3个事件
    start_element事件， 在读取 <a href="">时
    char_data event， 在读取python时
    end_element event, 在读取 </a>时
"""

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print 'sax-start_element: %s, attrs: %s' % (name, str(attrs))

    def end_element(self, name):
        print 'sax-end_element: %s' % name

    def char_data(self, data):
        print 'sax-char_data: %s' % data

xml = r"""<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
    <li><a href="/php">PHP</a></li>
</ol>
"""

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)





