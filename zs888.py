import xs
import os
import logging
from multiprocessing import Process
INTERPRETER = "C:/Users/Administrator/AppData/Local/Programs/Python/Python36-32/python.exe"

#import chardet


#timeB = [['19:46', '23:00']]

xss = [xs.xs('刀镇星河', 'http://www.sodu888.com/book/288771.html', [['10:30', '11:30'], ['12:00', '12:30'], ['17:00', '17:30']]),
       #xs.xs('刀镇星河', 'https://www.sodu.net/mulu_141978.html', [['9:10', '9:32'], ['11:54', '12:22'], ['16:54', '17:22']]),
       #xs.xs('极道天魔', 'http://www.soduso.com/mulu_3714707.html', [['16:36', '17:26']]),   #
       xs.xs('极道天魔', 'http://www.sodu888.com/book/295430.html', [['16:46', '17:30']]),   #
       xs.xs('蛊真人', 'http://www.sodu888.com/book/2705.html',[['19:46', '23:00']]),   #
       #xs.xs('蛊真人', 'http://www.soduso.com/mulu_3469590.html',[['20:09', '23:00']])
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

txt = open('D:/xs/蛊真人 请假一天.txt', encoding='utf-8')
all_the_text = txt.read( )
print(len(all_the_text))
print('end')
'''

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
