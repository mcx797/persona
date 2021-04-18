from url import Url
import os
import json

class Data:
    myUrl = Url("", "")

    def __init__(self, fileUrl):
        self.myUrl = fileUrl

    def openFile(self, fileUrl):
        f = open(fileUrl, 'r', encoding='utf-8')
        contain = json.loads(f.read())
        f.close()
        return contain

    def readCommit(self):
        commitListPath = self.myUrl.commitListPath()
        commitList = []
        for name in os.listdir(commitListPath):
            listC = self.openFile(commitListPath + '/' + name)
            for i in listC:
                commitList.append(i)
        return commitList

    def readIssue(self):
        issueListPath = self.myUrl.issueListPath()
        issueList = []
        for name in os.listdir(issueListPath):
            listC = self.openFile(issueListPath + '/' + name)
            for i in listC:
                issueList.append(i)
        return issueList

    def readSha(self):
        commitListPath = self.myUrl.commitListPath()
        commitList = []
        for name in os.listdir(commitListPath):
            listC = self.openFile(commitListPath + '/' + name)
            for i in listC:
                commitList.append(i['sha'])
        return commitList

    def readTree(self):
        commitListPath = self.myUrl.commitListPath()
        treeList = []
        for name in os.listdir(commitListPath):
            listC = self.openFile(commitListPath + '/' + name)
            for i in listC:
                treeList.append(i['commit']['tree'])
        return treeList


    def readIssueNumber(self):
        issueListPath = self.myUrl.issueListPath()
        issueList = []
        for name in os.listdir(issueListPath):
            listC = self.openFile(issueListPath + '/' + name)
            for i in listC:
                issueList.append(i['number'])
        return issueList