#-*-coding:utf-8 -*-
import io
import sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
from bs4 import BeautifulSoup

class doubanxingshu(object):
    def __init__(self):
        self.url = root_url
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
        self.bookname = []
        self.author = []
    
    def get_data(self):
        html = requests.get(self.url,headers=self.header)
        print(html.status_code)
        html.encoding = 'utf-8'
        soup = BeautifulSoup(html.text,'lxml')
        bookname = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > p:nth-child(3)')
        author = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)')
        
        print(html.apparent_encoding)
        for shuming in bookname:
            print(shuming.text)
    
        for author in author:
            print(author.string)
    
    #形成文件
        fout = open('豆瓣新书.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data1 in bookname:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data1.text)
            fout.write("</tr>")
        for data2 in author:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data2.text)
            fout.write("</tr>")

        fout.write("<table>")
        fout.write("</body>")
        fout.write("</html>")
        
if __name__ == "__main__":
    root_url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    wangye = doubanxingshu()
    wangye.get_data()

