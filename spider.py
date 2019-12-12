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
        self.fout = open('豆瓣新书速递.html','w')
    
    def get_data(self):
        html = requests.get(self.url,headers=self.header)
        content = html.text
        print(html.status_code)
        soup = BeautifulSoup(html.text,'lxml')
        shuming1 = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)')
        zhuozhe1 = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > p:nth-child(3)')
        jianjie1 = soup.select('.article > ul:nth-child(2) > li > div:nth-child(2) > p:nth-child(4)')
        shuming2 = soup.select('ul.pl20 > li > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)')
        zhuozhe2 = soup.select('ul.pl20 > li > div:nth-child(2) > p:nth-child(3)')
        jianjie2 = soup.select('ul.pl20 > li > div:nth-child(2) > p:nth-child(4)')
        print(html.apparent_encoding)
        b_a_j = []

        for x,y,z in zip(shuming1,zhuozhe1,jianjie1):
            print(x.text)
            print(y.text)
            print(z.text)
            b_a_j.append(x.text)
            b_a_j.append(y.text)
            b_a_j.append(z.text)
            
        for x,y,z in zip(shuming2,zhuozhe2,jianjie2):
            print(x.text)
            print(y.text)
            print(z.text)
            b_a_j.append(x.text)
            b_a_j.append(y.text)
            b_a_j.append(z.text)
           
        
        step = 3
        bookname_author_recommend = [b_a_j[i:i+step] for i in range(0,len(b_a_j),step)]
    
    #形成文件
        fout = open('豆瓣新书速递.html','w')
        self.fout.write(content.encode("gbk","ignore").decode("gbk","ignore"))
        
        fout.write("<!DOCTYPE html>\n")
        fout.write("<html lang='en'>\n")
        fout.write("<mate charset='UTF-8'>")
        fout.write("<head>")
        fout.write("<body style='text-aling:center;'>\n")
        fout.write("<h1 style='position:relative;top:20px;text-align:center;'>豆瓣新书速递</h1>")
        fout.write("<div style='position:relative;margin:auto;margin-top:5px;'>\n")

        i = 0
        for data in bookname_author_recommend:
            fout.write("<div style='position:relative;margin:top:100px;'>\n")
            for data in bookname_author_recommend[i]:
                fout.write("<p style='text-align:center;'>%s</p>\n"%data.encode(encoding='gbk',errors='ignore').decode("gbk","ignore"))
            i = i+1
            fout.write("</div>\n")

        fout.write("</div>\n")
        fout.write("</body>\n")
        fout.write("</head>")
        fout.write("</html>\n")
        fout.close()
        
if __name__ == "__main__":
    root_url = 'https://book.douban.com/latest?icn=index-latestbook-all'
    wangye = doubanxingshu()
    wangye.get_data()
