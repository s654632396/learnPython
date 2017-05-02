# coding=utf-8

from bs4 import BeautifulSoup
import re
import urlparse


class Parser(object):
    def parse(self, page_url, content):
        if page_url is None or content is None:
            return None
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        links = soup.find_all('a', href=re.compile(r'/item/[\s\S]+?'))
        new_urls = set()

        for link in links:
            new_url = link['href']
            full_url = urlparse.urljoin('http://baike.baidu.com', '%s') % new_url[1:]
            new_urls.add(full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = dict()

        res_data['url'] = page_url

        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data
