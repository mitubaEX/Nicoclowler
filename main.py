# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib
import datetime

d = datetime.datetime.today()

par_url = "http://www.nicovideo.jp/recent"

# urlアクセス
res = urllib2.urlopen(par_url)
# beautifulsoupでパース
soup = BeautifulSoup(res.read())

for link in soup.find_all('strong'):
    if str(d.year)+"年" in str(link):
        if str(d.month)+"月" in str(link):
            if str(d.day)+"日" in str(link):
                print link
            if str(d.day-1)+"日" in str(link):
                print link

# イメージファイルを取得
#for link in soup.find_all('img'):
#    ur = link.get('src')
#    str('ur')
#    if "tn-skr" in ur:
#        print ur

# 動画タイトルの取得
#for link in soup.find_all('a'):
#    ur_2 = link.get('title')
#    if ur_2:
#        print ur_2

# 動画URL取得
#for link in soup.find_all('a'):
#    ur_3 = link.get('href')
#    if "watch" in ur_3:
#        print "http://www.nicovideo.jp/"+ur_3


