import os
import string
import shutil
import datetime
import urllib.request

def main():
    today = datetime.date(2015, 5, 17)
    for i in range(20) :
        today = today + datetime.timedelta(days=1)
        load = 0;
        with open('../sysload/ips.code.txt') as ips:
            for ip in ips:
                load += processIpDate(ip.replace(' ', '').replace('\n', ''), today)
        with open('../sysload/load.csv', 'a') as csv:
            csv.write(str(today))
            csv.write(',')
            csv.write(str(load))
            csv.write('\n')
        print(str(today) + " " + str(load))

def processIpDate(ip, day):
    path = "../sysload/" + day.strftime('%Y%m%d') + "_" + ip + ".txt"
    catSource = ""
    with open(path) as catFile:
        catSource = catFile.read()
    try:
        begin = catSource.index(':[[')
        end = catSource.index(']],', begin)
        return sumLoad(catSource[begin + 3 : end])
        pass
    except Exception as e:
        print(path)
        print(e)
        pass
    return 0

def sumLoad(loadString):
    load = 0.0;
    for minuteLoad in loadString.split(','):
        load += float(minuteLoad)
    return load

main()