import xs
import os
import logging
from multiprocessing import Process
INTERPRETER = "C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/python.exe"

#import chardet


#timeB = [['19:46', '23:00']]

xss = [xs.xs('刀镇星河', 'http://www.sodu888.com/book/288771.html', [['8:00', '8:30'], ['12:00', '12:30']]),
       xs.xs('极道天魔', 'http://www.sodu888.com/book/295430.html', [['16:46', '17:30']]),   #
       xs.xs('蛊真人', 'http://www.sodu888.com/book/2705.html',[['19:46', '23:00']])
       ]
#checkToday888(jdtm)

def followBook(ith):
    print('正在追' + xss[ith].name)
    while True:
        xss[ith].checkToday()
        xss[ith].relax()

if __name__ == '__main__':
    for i in range(len(xss)):
        p = Process(target=followBook, args=(i,))
        p.start()

'''
while True:
    timeWork.relax()
    checkToday(timeWork)
'''

'''
html = requests.get(url)
selector = etree.HTML(html.text)
print(selector.xpath('//div[@id]'))
'''
