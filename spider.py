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
        shuming = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > p:nth-child(3)')
        zhuozhe = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)')
        print(html.apparent_encoding)
        author_bookname = []

        for x,y in zip(zhuozhe,shuming):
            print(x.text)
            print(y.text)
            author_bookname.append(x.text)
            author_bookname.append(y.text)
    
    #形成文件
        fout = open('豆瓣新书速递.html','w')
        
        fout.write("<!DOCTYPE html>\n")
        fout.write("<html lang='en'>\n")
        fout.write("<mate charset='UTF-8'>")
        fout.write("<head>")
        fout.write("<body style='text-aling:center;'>\n")
        fout.write("<table style='margin:auto;'>\n")

        for data in author_bookname:
            fout.write("<tr>\n")
            fout.write("<td style='text-align:center;'>%s</td>\n"%data)
            fout.write("</tr>\n")

        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</head>")
        fout.write("</html>\n")
        fout.close()
        
if __name__ == "__main__":
    root_url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    wangye = doubanxingshu()
    wangye.get_data()

