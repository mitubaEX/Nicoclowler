#! /usr/bin/ python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import xml.etree.ElementTree
import urllib2
import urllib
import datetime
import codecs
import os
import sys
import Tkinter
import re

root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("200x300")

def craw_anime(event):
    d = datetime.datetime.today()
    f = codecs.open("write.html","w",'utf-8')
    f.write("<html lang=\"ja\">"+'\n')
    f.write("<head>"+'\n')
    f.write("<title>sample</title>"+'\n')
    f.write("</head>"+'\n')
    f.write("<body>"+'\n')
    for n in range(1,10):
        if n == 1:
            par_url = "http://www.nicovideo.jp/tag/アニメ%20or%20ゲーム%20or%20東方%20or%20アイドルマスター%20or%20ラジオ%20or%20描いてみた?sort=n&order=d&ref=cate_comall"
        else:
            par_url = "http://www.nicovideo.jp/tag/アニメ+or+ゲーム+or+東方+or+アイドルマスター+or+ラジオ+or+描いてみた?page="+str(n)+"&sort=n&order=d"
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


def craw_music(event):
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

def craw_all(event):
    d = datetime.datetime.today()
    f = codecs.open("write.html","w",'utf-8')
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
    os.system("open write.html")

#ボタン
Button = Tkinter.Button(text=u'ALL', width=50)
Button.bind("<Button-1>",craw_all)
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button.pack()
Button3 = Tkinter.Button(text=u'アニメ・ゲーム', width=50)
Button3.bind("<Button-1>",craw_anime)
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button3.pack()
Button2 = Tkinter.Button(text=u'音楽・エンタメ', width=50)
Button2.bind("<Button-1>",craw_music)
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button2.pack()


root.mainloop()
