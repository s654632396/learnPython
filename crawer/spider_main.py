# coding=utf-8

from crawer import url_manager, html_outputer, html_downloader, html_parser


# 调度程序
class SpiderMain(object):

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.Downloader()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.Outputer()


    def craw(self, root_url, maxNum=1000):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'No.%d : %s' % (count, new_url)

                html_content = self.downloader.download(new_url)
                new_urls, new_content = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_content)
            except Exception, e:
                print 'craw failed : %d, %s' % (count, e)

            if count >= maxNum:
                break
            count += 1

        self.outputer.outputHTML()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, 300)
