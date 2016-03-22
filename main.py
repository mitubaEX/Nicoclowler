# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import urllib
import datetime
import codecs

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
            #print ur
    # 動画タイトルの取得
    for link in soup.find_all('a'):
        ur_2 = link.get('title')
        if ur_2:
            #print ur_2
            title_list.append(ur_2)
        # 動画URL取得
        ur_3 = link.get('href')
        if "watch" in ur_3:
            if flag == 0:
                #print "http://www.nicovideo.jp/"+ur_3
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
                        f.write(str(link)+'\n')
                        f.write("<a href=\""+"http://www.nicovideo.jp/"+str(href_list[j])+"\">"+str(title_list[j])+"</a>"+'\n')
                        f.write("<br>"+'\n')
                        #f.write(str(href_list[j])+'\n')
                        print link
                        print img_list[j]
                        print title_list[j]
                        print href_list[j]
                    #elif str(d.day-1)+"日" in str(link):
                    #    f.write(str(link))
                    #    f.write(str(img_list[j]))
                    #    f.write(str(title_list))
                    #    f.write(str(href_list[j]))
                    #    print link
                    #    print img_list[j]
                    #    print title_list[j]
                    #    print href_list[j]
            print j
            j += 1
        #del img_list[0]
        #del title_list[0]
        #del href_list[0]
f.write("</body>"+'\n')
f.write("</html>"+'\n')
f.close()

    #for i in range(0,30):
    #    print img_list[i]
    #    print title_list[i]
    #    print href_list[i]

