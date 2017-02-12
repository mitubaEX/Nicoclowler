#! /usr/bin/ python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import xml.etree.ElementTree
import urllib2
import urllib
from datetime import datetime, timedelta
import codecs
import os
import sys
import Tkinter
import re

from bottle import *


def craw_all():
    d = datetime.now()
    f = codecs.open("./views/write.html","w",'utf-8')
    f.write("<html lang=\"ja\">"+'\n')
    f.write("<head>"+'\n')
    f.write("<title>sample</title>"+'\n')
    f.write("</head>"+'\n')
    f.write("<body>"+'\n')
    for n in range(1,10):
        if n == 1:
            par_url = "http://www.nicovideo.jp/recent"
        else:
            par_url = "http://www.nicovideo.jp/recent?page="+str(n)
        # urlアクセス
        res = urllib2.urlopen(par_url)
        # beautifulsoupでパース
        soup = BeautifulSoup(res.read())
        title_list = []
        href_list = []
        img_list = []
        j = 0
        flag = 0
        # イメージファイルを取得
        for link in soup.find_all('img'):
            ur = link.get('src')
            str('ur')
            if "tn-skr" in ur:
                img_list.append(ur)
        # 動画タイトルの取得
        for link in soup.find_all('a'):
            ur_2 = link.get('title')
            if ur_2:
                title_list.append(ur_2)
            # 動画URL取得
            ur_3 = link.get('href')
            if "watch" in ur_3:
                if flag == 0:
                    href_list.append(ur_3)
                    flag = 1
                elif flag == 1:
                    flag = 0
        del title_list[0]
        del title_list[0]
        del title_list[0]

        for link in soup.find_all('strong'):
            if "<strong>2" in str(link):
                if str(d.year)+"年" in str(link):
                    if str(d.month)+"月" in str(link):
                        if str(d.day)+"日" in str(link) or str(d.day-1)+"日" in str(link):
                            f.write("<img src=\""+str(img_list[j])+"\" width=100 height=100>"+'\n')
                            f.write(str(link).decode('utf-8')+'\n')
                            f.write("<a href=\""+"http://www.nicovideo.jp/"+str(href_list[j]).decode('utf-8')+"\">")
                            f.write(unicode(title_list[j])+"</a>"+'\n')
                            f.write("<br>"+'\n')
                j += 1
    f.write("</body>"+'\n')
    f.write("</html>"+'\n')
    f.close()
    # os.system("open write.html")

@route('/')
def main():
    craw_all()
    return template('write')

run(host='localhost', port=8080, debug=True, reloader=True)
