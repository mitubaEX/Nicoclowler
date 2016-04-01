#! /usr/bin/ python
# -*- coding: utf-8 -*-
import urllib
import xml.etree.ElementTree
from bs4 import BeautifulSoup
import urllib2
import urllib
import datetime
import codecs
import os
import re

d = datetime.datetime.today()
f = codecs.open("write.html","w",'utf-8')
f.write("<html lang=\"ja\">"+'\n')
f.write("<head>"+'\n')
f.write("<title>sample</title>"+'\n')
f.write("</head>"+'\n')
f.write("<body>"+'\n')
for n in range(1,10):
    if n == 1:
        par_url = "http://www.nicovideo.jp/tag/エンターテイメント%20or%20音楽%20or%20歌ってみた%20or%20演奏してみた%20or%20踊ってみた%20or%20VOCALOID%20or%20ニコニコインディーズ?sort=n&order=d&ref=cate_comall"
    else:
        par_url = "http://www.nicovideo.jp/tag/エンターテイメント+or+音楽+or+歌ってみた+or+演奏してみた+or+踊ってみた+or+VOCALOID+or+ニコニコインディーズ?page="+str(n)+"&sort=n&order=d"
    # urlアクセス
    res = urllib2.urlopen(par_url)
    # beautifulsoupでパース
    soup = BeautifulSoup(res.read())
    title_list = []
    href_list = []
    img_list = []
    j = 0
    flag = 0

    # 動画タイトルの取得
    for link in soup.find_all('a'):
        # 動画URL取得
        ur_3 = link.get('href')
        if "watch" in ur_3:
            if flag == 0:
                if "search_tag_video" in ur_3:
                    print ur_3
                    u = re.split(r"[/:?]", ur_3)
                    print u[2]
                    ur = urllib.urlopen('http://ext.nicovideo.jp/api/getthumbinfo/' + str(u[2]))
                    x = ur.read()
                    e = xml.etree.ElementTree.XML(x)
                    thumb = list(e)[0]
                    title = thumb.find('title').text
                    #user_id = thumb.find('user_id').text
                    first_retrieve = thumb.find('first_retrieve').text
                    thumbnail_url = thumb.find('thumbnail_url').text
                    #tags = list(thumb.find('tags'))
                    print first_retrieve, title, thumbnail_url
                    # 曜日の切り抜き
                    tmp = first_retrieve.split('-')
                    tmp2 = tmp[2].split('T')
                    for m in tmp:
                        print m
                    print tmp2[0]
                    print
                    print d.year
                    print d.month
                    print d.day
                    print
                    if str(d.year) in str(tmp[0]):
                        if str(d.month) in str(tmp[1]):
                            if str(d.day) in str(tmp2[0]) or str(d.day-1)+"日" in str(tmp2[0]):
                                f.write("<img src=\""+str(thumbnail_url)+"\" width=100 height=100>"+'\n')
                                f.write(str(first_retrieve).decode('utf-8')+'\n')
                                f.write("<a href=\""+"http://www.nicovideo.jp/watch/"+str(u[2]).decode('utf-8')+"\">")
                                f.write(unicode(title)+"</a>"+'\n')
                                f.write("<br>"+'\n')
                #href_list.append(ur_3)
                flag = 1
            elif flag == 1:
                flag = 0

f.write("</body>"+'\n')
f.write("</html>"+'\n')
f.close()
os.system("open write.html")
