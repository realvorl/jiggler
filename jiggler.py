#!/usr/bin/env python3
import os
import sys
import time
import urllib
import datetime
from pyClasses import *
from pyPrometheus import *
from pyConsoleFormat import *
from urllib import request

listOfResults = []
expectations = limitsForTTFB(0.400, 2.150, 11.00)
refreshRate = 15
inputFile = '4timing.txt'


def evaluateStatus(status):
    if (status == 200):
        return good
    if (status < 500):
        return meh
    return bad


def evaluateResponse(time):
    if (time <= expectations.min):
        return good
    if (time < expectations.mid):
        return meh
    return bad


def timeToFirstByte(gCount, url):
    #writePrometheusHeader(gCount)
    start = time.time()
    status = 200
    ttfb = 0
    try:
        contents = request.urlopen(url)
        status = contents.status
        ttfb = (time.time() - start)
    except urllib.error.HTTPError as he:
        status = he.code
        ttfb = (time.time() - start)
    except urllib.error.URLError as ue:
        status = 666
        ttfb = 6.666
        url = "-> " + url

    #gauges[gCount].set(ttfb)

    listOfResults.append(formatedResponse(url, status, ttfb))
    #Prometheus.write_to_textfile


def makeARun():
    listOfResults[:] = []
    f = open(contentForPrometheus, "w")
    f.write("")
    f.close()
    with open(inputFile, 'r') as f:
        gCount = 0
        for url in f:
            timeToFirstByte(gCount, url.rstrip())
            gCount = gCount + 1


def andNowWeWait(thisLong):
    digits = len(str(thisLong - 1))
    delete = "\b" * (digits)
    for i in range(thisLong):
        print("{0}{1:{2}}".format(delete, (thisLong - i), digits), end="")
        time.sleep(1)
        sys.stdout.flush()
    print("\n Refreshing...")


def listMeUp():
    os.system('clear')
    dateStringed = str(
        datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    print("\t", "CODE  TTFB(s)   URL\t @" + dateStringed + "\n")
    for l in listOfResults:
        resultSerialized = l.asString()
        logFile = open("eternal.log", "a")
        logFile.write(dateStringed + " - " + resultSerialized + "\n")
        rgyStatus = evaluateStatus(l.status)
        rgyTime = evaluateResponse(l.ttfb)
        print("\t", stylize(" %s " % l.status, rgyStatus),
              stylize(" %.3f s " % l.ttfb, rgyTime), "%s \n" % l.url)


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        inputFile = str(sys.argv[1])
    while (True):
        makeARun()
        listMeUp()
        andNowWeWait(refreshRate)
