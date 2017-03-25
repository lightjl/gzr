import requests
from bs4 import BeautifulSoup
import re
import sendMail
import WorkInTime
import time
from datetime import datetime

class xs:
    def __init__(self):
        self.__new = ''

    def update(self, name):
        self.__new = name

    def isNew(self, name):
        return self.__new != name

    def newCharp(self):
        return self.__new

def checkToday(timeWork):  #
    login_seesion = requests.Session()
    url = 'http://www.sodu888.com'
    f = login_seesion.get(url+'/book/2705.html')
    # print(f.content.decode())

    soup = BeautifulSoup(f.content.decode(), "html.parser")
    #print(soup.prettify())
    #print(checkReaded)
    charpName = ''
    links = url+'/book/2705.html\n'
    #print(soup.body.table)
    newFlag = False
    for td in soup.findAll(attrs={"class": "time"}):
        if int(td.text[-2:]) < datetime.now().day:
            # 第一行更新小于当前时间，表面没更新
            break
        else:#更新了
            newFlag = True
            break
    if newFlag:
        numOneCharp = True
        links = url+'/book/2705.html\n'
        for charp in soup.findAll(rel=re.compile(r'nofollow')):
            if numOneCharp:
                numOneCharp = False
                if gzr.isNew(charp.text):   #找到更新章节名字
                    gzr.update(charp.text)
                else:   #跟新过了
                    break

            if not gzr.isNew(charp.text):   #最新章节
                links += url+charp['href']+'\n'
                pass
            else:                           #到了旧章节
                sendMail.sendMail(gzr.newCharp(), links)
                timeWork.changeRelaxTime(60*30) #跟新一章节后，半小时查看一次
                print(gzr.newCharp())
                print(links)
                break
    #print('well done')

print("蛊真人正在运行")
gzr = xs()
timeB = [['19:46', '23:00']]
timeWork = WorkInTime.WorkInTime(timeB, 64, 0)
while True:
    timeWork.relax()
    checkToday(timeWork)