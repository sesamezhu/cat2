import os
import string
import shutil
import datetime
import urllib.request

def main():
    with open('ips.code.txt') as ips:
        for ip in ips:
            processIp(ip.replace(' ', '').replace('\n', ''))

def processIp(ip):
    today = datetime.date.today()
    for i in range(21) :
        processDate(ip, today - datetime.timedelta(days=i))

def processDate(ip, day):
    tail = '&date=' + day.strftime('%Y%m%d') + '&ip=' + ip
    url = "http://cat.dianpingoa.com/cat/r/h?op=historyPart&domain=tuangou-mapi-web&reportType=day&type=extension&extensionType=System" + tail
    path = "../sysload/" + day.strftime('%Y%m%d') + "_" + ip + ".txt"
    if not os.path.exists(path):
        saveUrl(url, path) 

def saveUrl(url, path):  
    with open(path, 'wb') as text:
        text.write(urllib.request.urlopen(url).read())
    print(path)

main()