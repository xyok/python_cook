#!/usr/bin/python
#encoding:utf-8
'''
运用正则 多线程 队列 写简易的网络爬虫并下载文件
'''

import urllib
import os
import re
import requests
import threading
import Queue
import sys


class downthread(threading.Thread):
    def __init__(self,que,name):
	threading.Thread.__init__(self)
        self.que = que
        self.name = name
    def run(self):
        while 1:
            if not self.que.empty():
                furl = self.que.get()
                downfile(furl,self.name)
            else:
                break                 			
			
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
        #print 'one file downloaded'
    sys.stdout.write("downloading: [%s%s] %.2f%%\r" % ('#' * int(per/2), '-' * (50 - int(per/2)) , per))
    sys.stdout.flush()


#获取视频地址列表
def collect(url):
    #正则查找视频url
    url_r = r"(<a class=\"downbtn\" href=\')(http://mov\.bn\.netease\.com/open-movie/nos/mp4/2014/)(.*)(\.mp4)(\')"
    url_list = []
    r = requests.get(url)
    r_txt =r.text
    u = re.findall(url_r,r_txt)
    for n in u:
        url_list.append(n[1]+n[2]+n[3])
    return url_list

def downfile(f_url,n):
    url_l = f_url
    local = os.path.join(os.path.dirname(__file__),'vedio')
    #判断目录是否存在
    isExists = os.path.exists(local)
    if not isExists:
        os.mkdir(local)
    local_i = os.path.join(local,'%s.mp4' % n)
    urllib.urlretrieve(url_l,local_i,Schedule)	

def main():
    url = 'http://v.163.com/special/Khan/khanbiology.html'
    urllist = collect(url)
    vedio_sum = len(urllist)
    print "there are %d vedio in this page ." % vedio_sum
    num = input('how many vedio do you want to download?')
    tt = []
    que=Queue.Queue()
    for i in range(num):
        que.put(urllist[i])
    for i in range(num):
        d=downthread(que,i)
        d.start()
        tt.append(d)
    for t in tt:
        t.join()
    print "download complete ! files in your vedio directory"

if __name__=='__main__':
    main()
    
    
