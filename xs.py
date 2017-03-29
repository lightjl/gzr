from lxml import etree
import requests
import calendar
import sendMail
import time
import datetime
import getContent
import WorkInTime

class xs:
    def __init__(self, name, url, timeB):
        self.name = name
        self.__url = url
        self.__getContent = getContent.saveToFile()
        self.zjUrlHead = 'http://www.sodu888.com'
        self.timeB = timeB
        self.timeB.append(['23:59'] * 2)
        #print(self.timeB)
        self.wk = WorkInTime.WorkInTime(self.timeB, 60 * 10, 0)  # 休息10分钟

    def getUrl(self):
        return self.__url

    def isSave(self, filename):
        return self.__getContent.isDownloaded(filename)

    def save(self, filename, text):
        self.__getContent.save(filename, text)

    def sendToKindle(self, filename):
        sendMail.send_attachment_kd(self.__getContent.sub_folder, filename)

    def relax(self):
        self.wk.relax()

    def checkToday(self):
        url = self.getUrl()
        html = requests.get(url)
        selector = etree.HTML(html.text)
        # print(html.text)
        newFlag = False
        gxsj = selector.xpath('//td[@class="time"]/text()')

        if int(gxsj[0][-2:]) == datetime.datetime.now().day:  # 更新了
            newFlag = True

        if newFlag:
            zjs = selector.xpath('//a[@rel="nofollow"]')
            # print(zjs)
            for zj in zjs:
                zjName = (zj.xpath('./text()')[0])
                # print(zjName)
                zjGxsj = (zj.xpath('../../td[2]/text()')[0])
                # print(zjGxsj[-2:])
                if int(zjGxsj[-2:]) != datetime.datetime.now().day:
                    break
                zjHref = self.zjUrlHead + (zj.xpath('./@href')[0])
                # print(zjHref)
                if not (self.isSave(zjName)):
                    html = requests.get(zjHref)
                    html.encoding = 'utf-8'
                    selector = etree.HTML(html.content)

                    divs = (selector.xpath('//div[@id]'))
                    text = ''
                    for div in divs:
                        id = (div.xpath('@id'))[0]
                        if id == 'content' or id == 'contents' or id == 'txtContent':
                            # print(div.xpath('//text()'))
                            for eachP in (div.xpath('./text()')):
                                text += eachP + '\r\n'
                                pass
                    # print(text)
                    if text != '':
                        self.save(zjName, text)
                        self.sendToKindle(zjName)