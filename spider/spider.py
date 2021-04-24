from spider.url import Url
from spider.path import Path
from spider.saveFile import saveFile
import urllib.request
import json
import sys
import os


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
            if commitNumber < 100:
                break

    def spiderIssueList(self):
        Path(self.myUrl.issueListPath()).createPath()
        i = 1
        while True:
            path1 = Path(self.myUrl.issueLstConPath(i))
            if path1.pathExs():
                i += 1
                continue
            issueListiUrl = self.myUrl.issueLstiUrl(i)
            [issueNumber, strHtml] = self.spiderList(issueListiUrl)
            if issueNumber == 0:
                break
            saveFile(self.myUrl.issueLstConPath(i), strHtml)
            i += 1
            if issueNumber < 100:
                break

    def spiderContent(self, urlName):
        strHtml = urllib.request.urlopen(urlName).read()
        strHtml = str(strHtml, encoding='utf-8')
        return strHtml

    def spiderCommit(self, shaList):
        for Sha in shaList:
            commitPath = self.myUrl.commitPath(Sha)
            myPath = Path(commitPath)
            if not myPath.pathExs():
                strHtml = self.spiderContent(self.myUrl.commitUrl(Sha))
                saveFile(commitPath, strHtml)

    def spiderIssue(self, issueNumberList):
        for number in issueNumberList:
            issuePath = self.myUrl.issuePath(number)
            myPath = Path(issuePath)
            if not myPath.pathExs():
                strHtml = self.spiderContent(self.myUrl.issueUrl(number))
                saveFile(issuePath, strHtml)

    def spiderBlob(self, Blob):
        blobPath = self.myUrl.blobPath(Blob['sha'])
        myPath = Path(blobPath)
        if not myPath.pathExs():
            blobUrl = self.myUrl.blobUrl(Blob['url'])
            strHtml = self.spiderContent(blobUrl)
            saveFile(blobPath, strHtml)

    def spiderTree(self, treeList):
        n = 0
        treeNameIn = {}
        blobNameIn = {}
        for tree in treeList:
            treeNameIn[tree['sha']] = 1
        for tree in treeList:
            sha = tree['sha']
            treeUrl = self.myUrl.treeUrl(tree['url'])
            treePath = self.myUrl.treePath(sha)
            myPath = Path(treePath)
            if not myPath.pathExs():
                strHtml = self.spiderContent(treeUrl)
                saveFile(treePath, strHtml)
                strJson = json.loads(strHtml)
            else:
                f = open(self.myUrl.treePath(sha), 'r', encoding='utf-8')
                strJson = json.loads(f.read())
                f.close()
            for i in strJson['tree']:
                if i['type'] == 'tree':
                    if i['sha'] in treeNameIn.keys():
                        continue
                    treeList.append(i)
                    treeNameIn[i['sha']] = 1
                if i['type'] == 'blob':
                    if i['sha'] in blobNameIn.keys():
                        continue
                    self.spiderBlob(i)
                    blobNameIn[i['sha']] = 1
            n += 1
            print("n   = ", n)
            print("len =", len(treeList))

    def spiderDevl(self, developers):
        for key in developers:
            developerPath = self.myUrl.developerPath(key)
            myPath = Path(developerPath)
            if not myPath.pathExs():
                strHtml = self.spiderContent(self.myUrl.developerUrl(key))
                saveFile(developerPath, strHtml)