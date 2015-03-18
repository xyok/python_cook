#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

from PyQt4.QtGui import *
from PyQt4 import QtGui
from PyQt4 import QtCore

class TableWidget(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle('result of global alignment,reference only,designed by lj.F')

        jieguo = shuru()
        hen = jieguo[2]
        hen = ["0"]+hen
        zon = jieguo[3]
        zon = ["0"]+zon
        lzon = len(zon)
        lhen = len(hen)
        score = jieguo[0]
        lujin = huisu(jieguo[1])
        mo=len(jieguo[1])-1
        rlu=[(mo,mo)]+rightlujin(lujin)
        self.table = QTableWidget(lhen,lzon)
        self.table.setHorizontalHeaderLabels(hen)
        self.table.setVerticalHeaderLabels(zon)
        for i in range(self.table.rowCount()):
            for j in range(self.table.columnCount()):
                cnt = '%d' % score[j][i]
                newItem = QTableWidgetItem(cnt)
                if (i,j) in rlu:
                    newItem.setBackgroundColor(QColor(127,255,212))
                self.table.setItem(i,j,newItem)
        self.setCentralWidget(self.table)

      
def shuru():
    h=[]
    z=[]
    heng=raw_input("input sequence:")
    zong=raw_input("input another sequence:")
    global s_a,s_b,s_c
    s_a=input("score of match : ")
    s_b=input("score of mismatch : ")
    s_c=input("score of a gap : ")

    for i in heng.upper():
        h.append(i)
    for i in zong.upper(): 
        z.append(i)
    lengthh=len(h)
    lengthz=len(z)
    score=[[0 for i in range(lengthh+1)] for j in range(lengthz+1)]
    zt=[[0 for i in range(lengthh+1)] for j in range(lengthz+1)]
    for i in range(lengthh+1):
        score[0][i]=s_c * i
        zt[0][i]=[0,i-1]
        
    for i in range(lengthz+1):
        score[i][0]=s_c * i
        zt[i][0]=[i-1,0]    

    for i in range(lengthz+1):
        if i >0:
            for j in range(lengthh+1):
                if j > 0:
                    feng= get_score(i,j,h,z,score)
                    score[i][j] = feng[0]
                    zt[i][j]=feng[1]
    print score
    return score,zt,h,z  
 
def get_score(x,y,h,z,sco):       
    s_zk = sco[x][y-1] + s_c
    s_hk = sco[x-1][y] + s_c 
    if h[x-1] == z[y-1]:
        s_pipei = sco[x-1][y-1] + s_a 
    else:
        s_pipei = sco[x-1][y-1] + s_b 
    get_s = max([s_hk,s_zk,s_pipei])
    last_p = []
    if get_s == s_pipei:
        last_p.append((x-1,y-1))
    if get_s==s_zk:
        last_p.append((x,y-1))
    if get_s == s_hk:
        last_p.append((x-1,y))
    return get_s,last_p
    
def huisu(zt):
    w=zt[-1][-1]
    lujin=[]
    wf=w[0]
    x=wf[0]
    y=wf[1]
    while x>0 and y>0:
        wf=w[0]
        x=wf[0]
        y=wf[1]
        w=zt[x][y]
        lujin.append(wf)
    return lujin   

def rightlujin(lu):
    rightlu=[]
    for v in lu:
        v_y=v[0]
        v_x=v[1]
        rightlu.append((v_x,v_y))
    print rightlu
    print "only for reference,designed by lj.F. v.alpha.0.1"
    return rightlu

app = QApplication(sys.argv)
tb = TableWidget()
tb.show()
sys.exit(app.exec_())






