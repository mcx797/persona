from url import Url
from path import Path
import sys
import urllib.request
import os
import json
from saveFile import saveFile

class Spider:
    myUrl = Url("", "")

    def __init__(self, urlIn):
        self.myUrl = urlIn

    def spiderList(self, urlName):
        strHtml = urllib.request.urlopen(urlName).read()
        strHtml = str(strHtml, encoding='utf-8')
        return [len(json.loads(strHtml)), strHtml]

    def spiderCommitList(self):
        Path(self.myUrl.commitListPath()).createPath()
        i = 1
        while True:
            path1 = Path(self.myUrl.comLstConPath(i))
            if path1.pathExs():
                i += 1
                continue
            comListiUrl = self.myUrl.comLstiUrl(i)
            [commitNumber, strHtml] = self.spiderList(comListiUrl)
            if commitNumber == 0:
                break
            saveFile(self.myUrl.comLstConPath(i), strHtml)
            i += 1

