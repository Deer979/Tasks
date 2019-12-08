#-*-coding:utf-8 -*-
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
from bs4 import BeautifulSoup
import re


class baidu(object):
    def __init__(self):
        self.url = 'https://baike.baidu.com/item/网络爬虫/5162711?fromtitle=%E7%88%AC%E8%99%AB&fromid=22046949&fr=aladdin'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
    
    def get_h1(self):
        html = requests.get(self.url,headers=self.header)
        print(html.status_code)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text,'lxml')
        h1 = soup.select('html body.wiki-lemma.normal div.body-wrapper div.content-wrapper div.content div.main-content dl.lemmaWgt-lemmaTitle.lemmaWgt-lemmaTitle- dd.lemmaWgt-lemmaTitle-title h1')
        a = soup.select('html body.wiki-lemma.normal div.body-wrapper div.content-wrapper div.content div.main-content div.lemma-summary div.para')
        print(html.apparent_encoding)
        for h1 in h1:
            print(h1.text)
        for a in a:
            print(a.text)
        
if __name__ == "__main__":
    wangye = baidu()
    wangye.get_h1()

